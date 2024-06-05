import sys
sys.path.append("./")
import unittest
from pyidrogeo.api import *
# from pyidrogeo.models import Frana
import datetime
                        


# To run this you need a secrets.properties file in the workspace root with the following content:
#
# username=yourusername
# password=yourpassword



class TestIdrogeoApi(unittest.TestCase):
    franaTest = "006-50020-00".replace("-", "")

    # run login before all test methods
    @classmethod
    def setUpClass(cls):

        IdrogeoApiUrls().set_api_url('https://test.idrogeo.isprambiente.it/api')

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
        
        id = self.franaTest
        response = get_frana(self.token, id)

        self.assertIsInstance(response, dict)
        self.assertEqual(response['id_frana'], id)
        self.assertEqual(response['point'], [9.005147756523442, 44.814063686112206])
        self.assertEqual(response['toponimo'], "Polverola")
        self.assertIsNone(response['morti'])
    
    def test_frana_with_geom_get(self):
        if not self.runtests:
            return
        # get the token from the class
        token = self.token
        
        id = self.franaTest
        response = get_frana(token, id)

        self.assertIsInstance(response, dict)
        self.assertEqual(response['id_frana'], id)
        self.assertIsNotNone(response['geom_polygon'])

    def test_frana_revisions_get(self):
        if not self.runtests:
            return
        
        id = self.franaTest
        response = get_frana_revisions(self.token, id)
        
        self.assertIsInstance(response, list)
        self.assertTrue(len(response) > 1)
        self.assertEqual(response[0]['id_frana'], id)

    def test_frana_last_revision_get(self):
        if not self.runtests:
            return
        id = self.franaTest
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
        # fields = ['id', 'active', 'created', 'modified', 'extent', 'stato', 'user', 'modified_by', 'macroregione', 'regione', 
        #         'provincia', 'comune', 'tipo_movimento', 'id_frana']
        # or all default fields (same as above)
        # fields = []

        response = frana_filter_post(token, select=fields, limit=3, search_args=search_args)
        
        self.assertIsInstance(response, list)
        if len(fields) > 0:
            self.assertEqual(len(response[0]), len(fields)+1) # why the heck is 'cause' added?
        self.assertEqual(len(response), 3)

        # for frana in response:
        #     print(frana)

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

    def test_frana_put(self):
        if not self.runtests:
            return
        # get the token from the class
        id = self.franaTest
        response = get_frana(self.token, id)

        # get user id
        previous_user = response['modified_by']
        #{'id': 'fbf174d4-106d-11ea-89de-0242ac120003', 'email': 'regione.piemonte@isprambiente.it', 'lastname': 'piemonte', 'firstname': 'regione'}
        

        user = {'id': '872d63f2-4ce4-11ea-a9b4-0242ac120004', 
                #    'email': 'regione.piemonte@isprambiente.it', 
                   'lastname': 'Antonello', 
                   'firstname': 'Andrea'
                   }
        
        response['modified_by'] = user
        response['posizione_punto'] = 1
        response["accuratezza_posizione"]= "esatta"
        datetime_now = datetime.datetime.now()
        ts = datetime_now.strftime('%Y-%m-%dT%H:%M:%S%z')
        response['data_oss_certa'] = ts
        response["stato"] = "bozza"

        print(response)

        put_frana(self.token, id, response)

        response = get_frana(self.token, id)

        #! TODO check with idrogeo team
        # self.assertEqual(response['data_oss_certa'], ts)
        # self.assertEqual(response['modified_by']['id'], user['id'])



if __name__ == '__main__':
    unittest.main()