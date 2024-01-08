import unittest
from pyidrogeo.api import login, frana_filter_post, get_frana, put_frana, get_frana_revisions, get_frana_last_revision

# run with python3 -m unittest discover tests/

# test the login api
class TestLogin(unittest.TestCase):
    # run login before all test methods
    @classmethod
    def setUpClass(cls):
        # get user and pwd from local file secrets.properties
        with open('secrets.properties', 'r') as f:
            user = f.readline().strip().split('=')[1]
            pwd = f.readline().strip().split('=')[1]

        cls.runtests = user and pwd

        token = login(user, pwd)
        cls.token = token
        # print(token)
        assert isinstance(token, str)
        assert token != ''

    def test_frana_get(self):
        if not self.runtests:
            return
        # get the token from the class
        token = self.token
        
        id = '0010000400'
        response = get_frana(token, id)
        
        self.assertIsInstance(response, dict)
        self.assertEqual(response['id_frana'], id)


    def test_frana_revisions_get(self):
        if not self.runtests:
            return
        id = '0010000400'
        response = get_frana_revisions(self.token, id)
        
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0]['id_frana'], id)

        #! QUESTIONS:
        #! 1. per le revisioni non e' possibile dare set di colonne etc?
        #! 2. non vedo id della revisione nel result. Come faccio a chiamare una data revisione (secondo swagger si puo')

    def test_frana_last_revision_get(self):
        if not self.runtests:
            return
        id = '0010000400'
        response = get_frana_last_revision(self.token, id)
        
        self.assertIsInstance(response, dict)
        self.assertEqual(response['id_frana'], id)


    # test the frana filter api
    def test_frana_filter(self):
        if not self.runtests:
            return
        # get the token from the class
        token = self.token

        search_args = {
                # "provincia_nome": "ilike.*bolzano*",
            "tipo_movimento":"eq.2"
        }
        response = frana_filter_post(token, select=['id', 'id_frana', 'active', 'created'], limit=3, search_args=search_args)
        
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 3)

        print(response[0])
        


if __name__ == '__main__':
    unittest.main()