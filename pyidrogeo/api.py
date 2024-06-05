import os
import requests
from typing import List


class IdrogeoApiUrls:
    """Singleton class that holds the API URL."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(IdrogeoApiUrls, cls).__new__(cls, *args, **kwargs)
            
            # by default the test site is used
            cls._instance.API_URL = 'https://test.idrogeo.isprambiente.it/api'
            # if the env var testing is set to false, use the production api
            if os.environ.get('TESTING', 'true').lower() == 'false':
                cls._instance.API_URL = 'https://idrogeo.isprambiente.it/api'

        return cls._instance
    
    def use_test_api(self):
        self._instance.API_URL = 'https://test.idrogeo.isprambiente.it/api'

    def use_production_api(self):
        self._instance.API_URL = 'https://idrogeo.isprambiente.it/api'
    
    def set_api_url(self, url:str):
        self._instance.API_URL = url

    def get_api_url(self):
        return self._instance.API_URL

    def get_login_api(self):
        return self._instance.API_URL + '/user/login'
    
    def get_frana_api(self):
        return self._instance.API_URL + '/frana'
    
    def get_frana_filter_api(self):
        return self._instance.get_frana_api() + '/filter'
    
    def get_regions_api(self):
        return self._instance.API_URL + '/iffi/regioni'
    
    def get_provinces_api(self):
        return self._instance.API_URL + '/iffi/province'
    
    def get_municipalities_api(self):
        return self._instance.API_URL + '/iffi/comuni'
    



def login(username, password):
    """Login to the api and return the token."""
    print(f"Login to {IdrogeoApiUrls().get_api_url()} with {username}")
    response = requests.post(IdrogeoApiUrls().get_login_api(), json={
        'username': username,
        'password': password
    })

    if response.status_code != 200:
        raise Exception('Login failed')

    # print(response.json())
    return response.json()['token']

def get_frana(token:str, id:str):
    """Get a validated frana by id."""
    if not id:
        raise Exception('No id given')
    url = IdrogeoApiUrls().get_frana_api() + '/' + id
    response = requests.get(url, headers={
        'Authorization': 'Bearer ' + token
    })

    if response.status_code != 200:
        raise Exception(response.json())
    
    return response.json()

def get_frana_revisions(token:str, id:str):
    """Get the revisions of a frana by its id."""
    if not id:
        raise Exception('No id given')
    url = IdrogeoApiUrls().get_frana_api() + '/' + id + '/revisions'
    response = requests.get(url, headers={
        'Authorization': 'Bearer ' + token
    })

    if response.status_code != 200:
        raise Exception(response.json())
    
    return response.json()

def get_frana_last_revision(token:str, id:str):
    """Get the last revisions of a frana by its id."""
    if not id:
        raise Exception('No id given')
    url = IdrogeoApiUrls().get_frana_api() + '/' + id + '/last'
    response = requests.get(url, headers={
        'Authorization': 'Bearer ' + token
    })

    if response.status_code != 200:
        raise Exception(response.json())
    
    return response.json()

def put_frana(token:str, id:str, body:dict):
    """Modify a frana object by id."""
    if not id:
        raise Exception('No id given')
    response = requests.put(IdrogeoApiUrls().get_frana_api() + '/' + id, json=body, headers={
        'Authorization': 'Bearer ' + token
    })

    if response.status_code != 200:
        raise Exception(response.json())
    
def frana_filter_post(token:str, select:List[str]=None, order:List[str]=None, limit:int=10, offset:int=0, search_args:dict=None):
    """Post to the frana filter api and return the response."""
    params = {
        'limit': limit,
    }
    if offset > 0:
        params['offset'] = offset
    if select:
        params['select'] = ",".join(select)
    if order:
        params['order'] = ",".join(order)

    response = requests.post(IdrogeoApiUrls().get_frana_filter_api(), params=params, json=search_args, headers={
        'Authorization': 'Bearer ' + token
    })
    print(response)

    if response.status_code != 200:
        raise Exception(response.json())

    return response.json()
    
def get_regions(token:str, only_id_and_name:bool=True):
    """Get all the regions."""
    response = requests.get(IdrogeoApiUrls().get_regions_api(), headers={
        'Authorization': 'Bearer ' + token
    })

    if response.status_code != 200:
        raise Exception(response.json())
    
    if only_id_and_name:
        return [(r['uid'], r['nome']) for r in response.json()]
    return response.json()

def get_provinces(token:str, region_id:str=None, only_id_and_name_and_region:bool=True):
    """Get provinces."""
    
    url = IdrogeoApiUrls().get_provinces_api()
    params = {}
    if region_id:
        params['cod_reg'] = region_id
    response = requests.get(url, params=params, headers={
        'Authorization': 'Bearer ' + token
    })

    if response.status_code != 200:
        raise Exception(response.json())
    
    if only_id_and_name_and_region:
        return [(r['uid'], r['nome'], r['cod_reg']) for r in response.json()]
    return response.json()

def get_municipalities(token:str, region_id:str=None, province_id:str=None, only_id_and_name:bool=True):
    """Get municipalities."""
    
    url = IdrogeoApiUrls().get_municipalities_api()
    params = {}
    if province_id:
        params['cod_prov'] = province_id
    if region_id:
        params['cod_reg'] = region_id
    response = requests.get(url, params=params, headers={
        'Authorization': 'Bearer ' + token
    })

    if response.status_code != 200:
        raise Exception(response.json())
    
    if only_id_and_name:
        return [(r['uid'], r['nome']) for r in response.json()]
    return response.json()