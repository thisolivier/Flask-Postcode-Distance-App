import json
from flask import Flask, render_template, request
from clients import postcodesClient
from longlats import distance_between

app = Flask(__name__)
postcodes = None
store_names = None
locations = None

@app.route('/view_stores')
def get_stores_view():
  data = sorted(zip(store_names, postcodes, locations), 
                key= lambda val:val[0])
  message = "Arranged alphabetically"
  return render_template('stores.html', storeTableData = data, message = message)

@app.route('/get_stores', methods = ['GET'])
def _get_radial_stores():
  radial_postcode = request.args.get('postcode')
  radius = float(request.args.get('radius'))
  data = find_radial_stores(postcode = radial_postcode, 
                            radius = radius
                            )
  message = "Within {}km of the postcode {}, arranged North to South".format(radius, radial_postcode)         
  return render_template('stores.html', storeTableData = data, message = message)

def find_radial_stores(postcode, radius):
  start_location = postcodesClient.get_position_from(postcode)
  good_locations = []
  for index, value in enumerate(locations):
    if value is None:
      continue
    end_location = value
    if distance_between(start_location, end_location) <= radius:
      good_locations.append((store_names[index], postcodes[index], value))
  return sorted(good_locations, key= lambda locationTuple: locationTuple[2][1], reverse = True)

with open('./static/stores.json') as storesRaw:
    stores = json.load(storesRaw)
    store_names = list(map(lambda postcodeDict: postcodeDict['name'], stores))
    postcodes = list(map(lambda postcodeDict: postcodeDict['postcode'], stores))
    locations = postcodesClient.get_bulk_positions_from_array_of(postcodes)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=4000, debug=True)