from ksef_client.ksef_client.models.authorisation_challenge_response import AuthorisationChallengeResponse
from ksef_client.ksef_client.models.authorisation_challenge_request import AuthorisationChallengeRequest
from ksef_client.ksef_client.api.interfejsy_interaktywne_sesja import authorisation_challenge
from ksef_client.ksef_client.models.subject_identifier_by_type import SubjectIdentifierByType
from ksef_client.ksef_client.types import Response
from tools.KSeF_xml import KSeF_xml

def authorization_challange_call(client, identifier):
    data = dict(
        type = 'onip',
        identifier = identifier
    )
    
    context_identifier_type = SubjectIdentifierByType.from_dict(data)
    request_body = AuthorisationChallengeRequest(context_identifier=context_identifier_type)
    response: Response[AuthorisationChallengeResponse] = authorisation_challenge.sync_detailed(client=client, json_body=request_body) 
    return response 

def set_challenge(xml: KSeF_xml, challenge: str) -> KSeF_xml:
    element = xml.get_child_by_tag('Challenge')
    element.text = challenge
    return xml 