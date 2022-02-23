import requests
import json 
from api.common import get_header, get_xml
from api.consts import INIT_SESSION_TOKEN_REQUEST, TEST_ENDPOINT_URL 

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


def init_token(identifier, challange):
    xml = get_xml(INIT_SESSION_TOKEN_REQUEST)

    root = xml.getroot() 
    
    print(root)
    print(root.text)
    print(root.tag)
    print(root.attrib)

    # for field in root.findall('Challenge'):
    #     print(f'field: {field}')
    #     field.text = 'moj test challenge'

    
    xml.write('out_test.xml')