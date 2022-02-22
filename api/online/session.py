import requests
import json 
from api.common import get_header
from api.consts import TEST_ENDPOINT_URL 

def authorisation_challenge(type = 'onip', identifier = '1111111111'):
    
    data = {
        "contextIdentifier": {
            "type": type,
            "identifier": identifier
        }
    }

    endpoint = f"{TEST_ENDPOINT_URL}api/online/Session/AuthorisationChallenge"
    response = requests.post(endpoint, data=json.dumps(data), headers=get_header())
    response.raise_for_status( )

    return response.status_code, response.json()
