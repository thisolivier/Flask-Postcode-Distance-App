import requests


class _PostcodesClient:
  _base_url = "https://api.postcodes.io/postcodes"
  
  def get_position_from(self, postcode):
      """Get long and latitude as a tuple from a postcode string"""
      response = requests.get(self._base_url + "/{}".format(postcode))
      if response.status_code == 200:
          decoded_result = response.json()['result']
          print(decoded_result)
          return (decoded_result['longitude'], decoded_result['latitude'])
      else:
          raise Exception("Bad response from postcode.io, status:", response.status_code)

  def get_bulk_positions_from_array_of(self, postcodes):
      """Get long and lat tuples as a list from a list of postcodes"""
      response = requests.post(self._base_url, data = {'postcodes': postcodes})
      if response.status_code == 200:
          # Ensure every requested postcode will have an entry
          results_dict = dict.fromkeys(postcodes, None)
          decoded_results = response.json()['result']
          for result in decoded_results:
              if result['result'] is not None:
                  results_dict[result['query']] = (
                      result['result']['longitude'], 
                      result['result']['latitude'],)
          # Ensure ordering of return list
          return_list = []
          for postcode in postcodes:
              return_list.append(results_dict[postcode])
          return return_list
      else:
          raise Exception("Bad response from postcode.io, status:", response.status_code)


postcodesClient = _PostcodesClient()