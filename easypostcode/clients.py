import requests


class _PostcodesClient:
    _base_url = "https://api.postcodes.io/postcodes"
  
    def get_position_from(self, postcode):
        """Get longitude and latitude coordinates from a postcode

        - param - postcode -- A string matching postcode formatting
        - return -- Tuples contaning location as (longitude, latitude) floats
        """

        response = requests.get(self._base_url + "/{}".format(postcode))
        if response.status_code == 200:
            decoded_result = response.json()['result']
            return (decoded_result['longitude'], decoded_result['latitude'])
        else:
            raise Exception("Bad response from postcode.io, status:", 
                response.status_code)

    def get_bulk_positions_from_array_of(self, postcodes):
        """Get long and lat tuples as a list, from a list of postcodes
        
        - param - postcodes -- A list of strings matching postcode format
        - return -- A list of long and lat tuples in same order as postcodes
        """
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


class MockPostcodesClient:

    def __init__(self, single_positon, bulk_posiitons):
        self.position = single_positon
        self.positions = bulk_posiitons
  
    def get_position_from(self, postcode):
        return self.position

    def get_bulk_positions_from_array_of(self, postcodes):
        returnList = []
        for index in range(0, len(postcodes)):
            if index < len(self.positions):
                returnList.append(self.positions[index])
            else:
                returnList.append(None)
        return returnList


postcodesClient = _PostcodesClient()