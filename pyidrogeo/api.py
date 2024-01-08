import os
import requests

# main api constants
API_URL = 'https://test.idrogeo.isprambiente.it/api'

# if the env var testing is set to false, use the production api
if os.environ.get('TESTING', 'true').lower() == 'false':
    API_URL = 'https://idrogeo.isprambiente.it/api'

# msain api urls
LOGIN_API = API_URL + '/user/login'
FRANA_API = API_URL + '/frana'
FRANA_FILTER_API = FRANA_API + '/filter'
REGIONS_API = API_URL + '/iffi/regioni'
PROVINCES_API = API_URL + '/iffi/province'
MUNICIPALITIES_API = API_URL + '/iffi/comuni'

def login(username, password):
    """Login to the api and return the token."""
    response = requests.post(LOGIN_API, json={
        'username': username,
        'password': password
    })

    if response.status_code != 200:
        raise Exception('Login failed')

    # print(response.json())
    return response.json()['token']

def get_frana(token:str, id:str):
    """Get a frana by id."""
    if not id:
        raise Exception('No id given')
    url = FRANA_API + '/' + id
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
    url = FRANA_API + '/' + id + '/revisions'
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
    url = FRANA_API + '/' + id + '/last'
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
    response = requests.put(FRANA_API + '/' + id, json=body, headers={
        'Authorization': 'Bearer ' + token
    })

    if response.status_code != 200:
        raise Exception(response.json())
    
def frana_filter_post(token:str, select:[str]=None, order:[str]=None, limit:int=10, offset:int=0, search_args:dict=None):
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

    response = requests.post(FRANA_FILTER_API, params=params, json=search_args, headers={
        'Authorization': 'Bearer ' + token
    })
    print(response)

    if response.status_code != 200:
        raise Exception(response.json())

    return response.json()
    
def get_regions(token:str, only_id_and_name:bool=True):
    """Get all the regions."""
    response = requests.get(REGIONS_API, headers={
        'Authorization': 'Bearer ' + token
    })

    if response.status_code != 200:
        raise Exception(response.json())
    
    if only_id_and_name:
        return [(r['uid'], r['nome']) for r in response.json()]
    return response.json()

def get_provinces(token:str, region_id:str=None, only_id_and_name_and_region:bool=True):
    """Get provinces."""
    
    url = PROVINCES_API
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
    
    url = MUNICIPALITIES_API
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