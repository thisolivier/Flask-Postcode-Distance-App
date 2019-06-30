import json
from os.path import join, dirname, realpath

from flask import Flask, render_template, request

from easypostcode.clients import postcodesClient
from easypostcode.longlats import distance_between

app = Flask(__name__)
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


@app.route('/get_stores', methods = ['GET'])
def _get_radial_stores():
    radial_postcode = request.args.get('postcode')
    radius = float(request.args.get('radius'))
    locations = find_radial_stores(
        postcode = radial_postcode, 
        radius = radius)
    data = sorted(
        locations, 
        key= lambda locationTuple: locationTuple[2][1], 
        reverse = True)
    message = "Within {}km of the postcode {}, arranged North to South".format(
        radius, 
        radial_postcode)
    return render_template(
        'stores.html', 
        storeTableData = data, 
        message = message)


def find_radial_stores(postcode, radius):
    """Given a postcode and radius, returns stores within that radius

    Keyword Arguments:
    postcode -- A string matching postcode formatting
    radius -- A number representing the kilometers from the postcode to search

    Returns:
    good_locations_list -- List of tuples contaning name, postcode and location tuple
    """
    start_location = postcodesClient.get_position_from(postcode)
    good_locations = []
    for index, end_location in enumerate(locations):
        if (end_location is not None and 
                distance_between(
                    start_location, 
                    end_location) 
                <= radius):
            good_locations.append(
                (store_names[index], postcodes[index], end_location,))
    return good_locations


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
    locations = postcodesClient.get_bulk_positions_from_array_of(postcodes)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)