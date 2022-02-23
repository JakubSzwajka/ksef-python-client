import ast
import json
from api.consts import TEST_ENDPOINT_URL, TOKEN_INIT_FILE, XML_SAMPLES_ROOT
from api.common import get_header, update_challenge
from ksef_client.ksef_client import Client
from ksef_client.ksef_client.models.authorisation_challenge_response import AuthorisationChallengeResponse
from ksef_client.ksef_client.models.authorisation_challenge_request import AuthorisationChallengeRequest
from ksef_client.ksef_client.api.interfejsy_interaktywne_sesja import authorisation_challenge
from ksef_client.ksef_client.models.subject_identifier_by_type import SubjectIdentifierByType
from ksef_client.ksef_client.types import Response


from ksef_client.ksef_client.models.init_session_token import InitSessionTokenRequest 
from ksef_client.ksef_client.api.interfejsy_interaktywne_sesja import init_session_token
from ksef_client.ksef_client.models.init_session_response import InitSessionResponse


if __name__ == '__main__':
    data = {
        "type": 'onip',
        "identifier": '1111111111'
    }

    client = Client(base_url=TEST_ENDPOINT_URL, headers=get_header( ))
    context_identifier_type = SubjectIdentifierByType.from_dict(data)

    request_body = AuthorisationChallengeRequest(context_identifier=context_identifier_type)
    response: Response[AuthorisationChallengeResponse] = authorisation_challenge.sync_detailed(client=client, json_body=request_body) 

    print(response.content)
    response_data = ast.literal_eval(response.content.decode('UTF-8')) 
    print(response_data)
    challenge = response_data.get('challenge')
    # challenge = '12321'

    # update_challenge(TOKEN_INIT_FILE, challenge)
    
    body = InitSessionTokenRequest(path=XML_SAMPLES_ROOT + TOKEN_INIT_FILE, challenge=challenge)
    response: Response[InitSessionResponse] = init_session_token.sync_detailed(client=client, request_body=body)

    print(response.content)