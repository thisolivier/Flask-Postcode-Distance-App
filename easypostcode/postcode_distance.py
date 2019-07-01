import json
from os.path import join, dirname, realpath

from flask import Flask, render_template, request

from easypostcode.clients import postcodesClient
from easypostcode.longlats_helper import distance_between

app = Flask(__name__)
client = postcodesClient
stores_path = join(dirname(realpath(__file__)), 'static/stores.json')
postcodes = None
store_names = None
locations = None

@app.route('/view_stores')
def get_stores_view():
    data = sorted(
        zip(
            store_names, 
            postcodes, 
            locations), 
        key= lambda val:val[0])
    message = "Arranged alphabetically"
    return render_template(
        'stores.html', 
        storeTableData = data, 
        message = message)


@app.route('/view_nearby_stores', methods = ['GET'])
def _get_radial_stores():
    data = [[],[],[]]
    # Check arguments
    if 'postcode' in request.args and 'radius' in request.args:
        radial_postcode = request.args.get('postcode')
        radius = request.args.get('radius')
        try:
            radius = float(request.args.get('radius'))
            # Get locations
            data = find_radial_stores(
                postcode = radial_postcode, 
                radius = radius)
            # Prepare template message
            message = "Within {}km of the postcode {}, \
                arranged North to South".format(radius, radial_postcode)
        except ValueError:
            message = "Your radius was not a number, please try again"
    else:
        message = "Correct arguments not found, please check your query"
    return render_template(
        'stores.html', 
        storeTableData = data, 
        message = message)


def find_radial_stores(postcode, radius):
    """Given a postcode and radius, returns stores within that radius

    - param - postcode -- A string matching postcode formatting
    - param - radius -- A number of kilometers from the postcode to search
    - return -- List of tuples contaning name, postcode and (long, lat) tuple
    """
    start_location = client.get_position_from(postcode)
    good_locations = []
    for index, end_location in enumerate(locations):
        if (end_location is not None and 
                distance_between(
                    start_location, 
                    end_location) 
                <= radius):
            good_locations.append(
                (store_names[index], postcodes[index], end_location,))
    return sorted(
                good_locations, 
                key= lambda locationTuple: locationTuple[2][1], 
                reverse = True)


# New to flask, can see moving the static stores to a class, making it easier to test
# But, not sure how to have remote store which needs initialising and yet keep app stateless
with open(stores_path) as storesRaw:
    stores = json.load(storesRaw)
    store_names = list(
        map(
        lambda postcodeDict: postcodeDict['name'], 
        stores))
    postcodes = list(
        map(
        lambda postcodeDict: postcodeDict['postcode'], 
        stores))
    locations = client.get_bulk_positions_from_array_of(postcodes)

# Launch flask app with data from stores, if we're main
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)