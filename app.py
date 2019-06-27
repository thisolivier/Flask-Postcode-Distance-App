from flask import Flask
app = Flask(__name__)
postcode_positions = None

class postcodesClient:
  # param:postcode - A string matching postcode formatting
  def getPositionFrom(postcode):
    return (0,0)

  # param:postcodes - Array of strings matching postcode formatting
  def getBulkPositionsFromArrayOf(postcodes):
    return [(0,0),(1,1)]

def get_postcode_positions():
  # Should query postcodes.io for the positions
  # Should save them in memory as a dict 
  #   using the postcode as a key
  #   using tuple for long and lat as the value
  pass

@app.route('/view_stores')
def get_stores_view():
  # Should list stores alphabetically
  # Should query postcodes.io to get long and lat
  # Should update the view with the longs and lats
  # Template should reload ever 5s is postcodes not yet loaded
  pass

@app.route('/get_stores', methods = ['GET'])
def find_radial_stores():
  # Should check input for a postcode and radius
  #A Should query for the log and lat new postcode
  #B Should check postcodes have loaded
    # Once A&B
    # Zip

