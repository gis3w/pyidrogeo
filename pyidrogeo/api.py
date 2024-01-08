import os
import requests

# main api constants
API_URL = 'https://test.idrogeo.isprambiente.it/api'

# if the env var testing is set to false, use the production api
if os.environ.get('TESTING', 'false').lower() == 'false':
    API_URL = 'https://idrogeo.isprambiente.it/api'

# msain api urls
LOGIN_API = API_URL + '/user/login'
FRANA_API = API_URL + '/frana'
FRANA_FILTER_API = FRANA_API + '/filter'

def login(username, password):
    """Login to the api and return the token."""
    response = requests.post(LOGIN_API, json={
        'username': username,
        'password': password
    })

    if response.status_code != 200:
        raise Exception('Login failed')

    return response.json()['token']

def get_frana(token:str, id:str):
    """Get a frana by id."""
    if not id:
        raise Exception('No id given')
    response = requests.get(FRANA_API + '/' + str(id), headers={
        'Authorization': 'Bearer ' + token
    })

    if response.status_code != 200:
        raise Exception(response.json())
    
    return response.json()

def put_frana(token:str, id:str, body:dict):
    """Modify a frana object by id."""
    if not id:
        raise Exception('No id given')
    response = requests.put(FRANA_API + '/' + str(id), json=body, headers={
        'Authorization': 'Bearer ' + token
    })

    if response.status_code != 200:
        raise Exception(response.json())
    
def frana_filter_post(token:str, select:[str]=None, order:[str]=None, limit:int=10, offset:int=0, ):
    """Post to the frana filter api and return the response."""
    body = {
        'limit': limit,
    }
    if offset > 0:
        body['offset'] = offset
    if select:
        body['select'] = ",".join(select)
    if order:
        body['order'] = ",".join(order)

    response = requests.post(FRANA_FILTER_API, json=body, headers={
        'Authorization': 'Bearer ' + token
    })
    print(response)

    if response.status_code != 200:
        raise Exception(response.json())

    return response.json()
    

