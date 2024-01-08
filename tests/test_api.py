import unittest
from pyidrogeo.api import login, frana_filter_post, get_frana, put_frana, get_frana_revisions, get_frana_last_revision,get_regions, get_provinces, get_municipalities
                        


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

    def test_frana_put(self):
        if not self.runtests:
            return
        # get the token from the class
        id = '0010000400'
        response = get_frana(self.token, id)

        #! QUESTIONS
        #! this does not work like that. Seems to need some mandatory fields

        user_id = '872d63f2-4ce4-11ea-a9b4-0242ac120004'
        response['modified_by'] = user_id
        put_frana(self.token, id, response)

        response = get_frana(self.token, id)
        self.assertEqual(response['modified_by'], user_id)


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


    def test_frana_filter(self):
        if not self.runtests:
            return
        # get the token from the class
        token = self.token

        search_args = {
                "provincia_nome": "ilike.*Torino*",
            "tipo_movimento":"eq.2"
        }
        # a selection of fields
        fields = ['id', 'id_frana', 'active', 'created', 'provincia']
        # or all available fields
        fields = ['id', 'active', 'created', 'modified', 'extent', 'stato', 'user', 'modified_by', 'macroregione', 'regione', 
                'provincia', 'comune', 'tipo_movimento', 'id_frana']
        #! QUESTIONS:
        #! dove sono tutti gli altri campi che si possono settare della frana?
        
        # or all default fields (same as above)
        # fields = []

        response = frana_filter_post(token, select=fields, limit=3, search_args=search_args)
        
        self.assertIsInstance(response, list)
        if len(fields) > 0:
            self.assertEqual(len(response[0]), len(fields)+1) # why the heck is 'cause' added?
        self.assertEqual(len(response), 3)

        for frana in response:
            print(frana)

    def test_get_regions(self):
        if not self.runtests:
            return
        response = get_regions(self.token)
        
        self.assertIsInstance(response, list)
        self.assertEqual(len(response[0]), 2)
        self.assertEqual(len(response), 20)

    def test_get_provinces(self):
        if not self.runtests:
            return
        response = get_provinces(self.token)
        
        self.assertIsInstance(response, list)
        self.assertEqual(len(response[0]), 3)
        self.assertEqual(len(response), 107)

        # try only T-AA
        response = get_provinces(self.token, region_id='4')
                
        self.assertIsInstance(response, list)
        self.assertEqual(len(response[0]), 3)
        self.assertEqual(len(response), 2)

    def test_get_municipalities(self):
        if not self.runtests:
            return
        response = get_municipalities(self.token)
        
        self.assertIsInstance(response, list)
        self.assertEqual(len(response[0]), 2)
        self.assertEqual(len(response), 7904)

        # try only T-AA
        response = get_municipalities(self.token, region_id='4')
                
        self.assertIsInstance(response, list)
        self.assertEqual(len(response[0]), 2)
        self.assertEqual(len(response), 282)

        
        # try only AA
        response = get_municipalities(self.token, region_id='4', province_id='21')
                
        self.assertIsInstance(response, list)
        self.assertEqual(len(response[0]), 2)
        self.assertEqual(len(response), 116)



if __name__ == '__main__':
    unittest.main()