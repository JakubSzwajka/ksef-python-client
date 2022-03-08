import ast
from api.consts import SIGN_INIT_FILE, TEST_ENDPOINT_URL, TOKEN_INIT_FILE, XML_SAMPLES_ROOT
from api.common import get_header
from ksef_client import ksef_client
from ksef_client.ksef_client import Client
from ksef_client.ksef_client.models.authorisation_challenge_response import AuthorisationChallengeResponse
from ksef_client.ksef_client.models.authorisation_challenge_request import AuthorisationChallengeRequest
from ksef_client.ksef_client.api.interfejsy_interaktywne_sesja import authorisation_challenge
from ksef_client.ksef_client.models.subject_identifier_by_type import SubjectIdentifierByType
from ksef_client.ksef_client.types import Response


from ksef_client.ksef_client.models.init_session_signed import InitSessionSignedRequest 
from ksef_client.ksef_client.api.interfejsy_interaktywne_sesja import init_session_signed
from ksef_client.ksef_client.models.init_session_response import InitSessionResponse

from KSeF_xml import KSeF_xml

IDENTIFIER = '1111111112'

def main():
    
    data = {
        "type": 'onip',
        "identifier": IDENTIFIER
    }
    
    client = create_client(TEST_ENDPOINT_URL, header=get_header( ))
    response = authorization_challange_call(client, data)
    r_data = get_response_data(response)
    
    CHALLANGE = r_data.get('challenge')
    
    xml: KSeF_xml = KSeF_xml(XML_SAMPLES_ROOT + SIGN_INIT_FILE)
    xml = set_challenge(xml, CHALLANGE)

    body = InitSessionSignedRequest(bytes=xml.to_bytes())
    response: Response[InitSessionResponse] = init_session_signed.sync_detailed(client=client, request_body=body)

    r_data = get_response_data(response)
    

def authorization_challange_call(client, data):
    context_identifier_type = SubjectIdentifierByType.from_dict(data)
    request_body = AuthorisationChallengeRequest(context_identifier=context_identifier_type)
    response: Response[AuthorisationChallengeResponse] = authorisation_challenge.sync_detailed(client=client, json_body=request_body) 
    return response 

def set_identifier(xml: KSeF_xml, identifier: str) -> KSeF_xml:
    element = xml.get_child_by_tag('Identifier', namespace= 'ns2')
    element.text = identifier
    return xml 

def set_challenge(xml: KSeF_xml, challenge: str) -> KSeF_xml:
    element = xml.get_child_by_tag('Challenge')
    element.text = challenge
    return xml 

def init_signed():
    pass 

def create_client(url, header):
    return Client(base_url=url, headers=header)

def get_response_data(response, print_data = True):
    try:
        response_data = ast.literal_eval(response.content.decode('UTF-8'))     
        if print_data:
            print(response_data)
    except ValueError as e:
        print(e)
        print('----------')
        print(response)
        return response 
    return response_data

if __name__ == '__main__':
    main( )
    
    
    
    """
    
        08.03.2022 SKONCZYLEM 
        
        {'timestamp': '2022-03-08T21:41:35.398Z', 'challenge': '20220308-CR-999C6F2A46-575329CFB5-48'}
{'exception': 
{'serviceCtx': 'srvTEMFA', 
'serviceCode': '20220308-EX-3A85AC36EB-C975A4EED0-DD', 
'serviceName': 'online.session.session.signed.init', 
'timestamp': '2022-03-08T21:41:35.615Z', 
'referenceNumber': '20220308-SE-356EB69A0C-DE44117973-3E', 
'exceptionDetailList': [{'exceptionCode': 9102, 
'exceptionDescription': 'Brak podpisu.'}]}}
    
    
    
    """