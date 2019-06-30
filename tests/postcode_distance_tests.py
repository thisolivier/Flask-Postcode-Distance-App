import os
import tempfile
import unittest

from context import postcode_distance
from context import clients

class PostcodeDistanceTest(unittest.TestCase):
    # function to set up testing connection
    def setUp(self):
        postcode_distance.app.config["TESTING"] = True
        postcode_distance.app.config["DEBUG"] = True
        postcode_distance.store_names = ["A","B","C","D","E","F"]
        postcode_distance.postcodes = ["Ps1","Ps2","Ps3","Ps4","Ps5","Ps6"]
        postcode_distance.client = clients.mockPostcodesClient
        postcode_distance.locations = clients.mockPostcodesClient.get_bulk_positions_from_array_of(postcode_distance.postcodes)
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
    
    def test_find_radial_stores(self):
        # Mock client always returns location 3,3, which will be position of postccode
        result = postcode_distance.find_radial_stores('XYZ', 1)
        assert result[0][2] == (3,3)

if __name__ == "__main__":
    unittest.main()