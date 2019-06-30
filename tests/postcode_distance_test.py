import os
import tempfile
import unittest

from context import postcode_distance

class PostcodeDistanceTest(unittest.TestCase):
    # function to set up testing connection
    def setUp(self):
        postcode_distance.app.config["TESTING"] = True
        postcode_distance.app.config["DEBUG"] = True
        self.app = postcode_distance.app.test_client()
        self.assertEqual(postcode_distance.app.debug, False)

    # function to teardown connection after testing
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()