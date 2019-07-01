import os
import tempfile
import unittest

from context import postcode_distance
from context import clients

class PostcodeDistanceTest(unittest.TestCase):
    static_location = (-0.91732, 52.38135,) # NN6 9JE
    bulk_locations = [
        (-0.68624, 52.29448,), # NN8 2DJ - 27.5km away
        (-0.412008, 52.38135,), # MK44 2BE - 58.2km away
        (-1.595903, 52.191168,)] # NN6 9JE - 78.4km away

    # function to set up testing connection
    def setUp(self):
        postcode_distance.app.config["TESTING"] = True
        postcode_distance.app.config["DEBUG"] = True
        postcode_distance.store_names = ["A","B","C"]
        postcode_distance.postcodes = ["NN8 2DJ", "MK44 2BE", "NN6 9JE"]
        postcode_distance.client = clients.MockPostcodesClient(
            self.static_location, self.bulk_locations)
        # This line is apocraphal and should not be needed
        postcode_distance.locations = postcode_distance.client.get_bulk_positions_from_array_of(postcode_distance.postcodes)

        self.app = postcode_distance.app.test_client()
        self.assertEqual(postcode_distance.app.debug, True)

    # function to teardown connection after testing
    def tearDown(self):
        pass

    def test_view_all_stores(self):
        response = self.app.get('/view_stores')
        assert response.status_code == 200

    def test_view_nearby_stores(self):
        response = self.app.get('/view_nearby_stores?postcode=SW19 5DF&radius=20')
        assert response.status_code == 200
        response = self.app.get('/view_nearby_stores')
        assert response.status_code == 200
        response = self.app.get('/view_nearby_stores?postcode=SW19 5DF&radius=foo')
        assert response.status_code == 200
    
    def test_find_radial_stores_quantity(self):
        # Mock client created with data in head
        result = postcode_distance.find_radial_stores('Query', 10)
        assert len(result) == 0
        result = postcode_distance.find_radial_stores('Query', 40)
        assert len(result) == 1
    
    def test_find_radial_stores_ordering(self):
        # Mock client created with data in head
        result = postcode_distance.find_radial_stores('Query', 80)
        assert len(result) == 3
        assert result[0][2][1] > result[1][2][1]
        assert result[1][2][1] > result[2][2][1]

if __name__ == "__main__":
    unittest.main()