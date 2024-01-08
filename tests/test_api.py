import unittest
from pyidrogeo.api import login, frana_filter_post, get_frana, put_frana

# run with python3 -m unittest discover tests/

# test the login api
class TestLogin(unittest.TestCase):
    # run login before all test methods
    @classmethod
    def setUpClass(cls):
        token = login('andrea.antonello@gmail.com', 'ck%77$zPgpH')
        cls.token = token
        # assert it is a string
        assert isinstance(token, str)
        # assert it is not empty
        assert token != ''

    # test the get frana method
    def test_frana_get(self):
        # get the token from the class
        token = self.token
        print(token)
        response = get_frana(token, 1)
        
        self.assertIsInstance(response, dict)
        self.assertEqual(response['id'], 1)


    # test the frana filter api
    def test_frana_filter(self):
        # get the token from the class
        token = self.token
        print(token)
        response = frana_filter_post(token, limit=3)
        
        self.assertIsInstance(response, dict)
        self.assertEqual(len(response), 3)
    
        


if __name__ == '__main__':
    unittest.main()