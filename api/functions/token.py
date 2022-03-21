from ksef_client.ksef_client.models.credentials_role_request_token_type import CredentialsRoleRequestTokenType
from ksef_client.ksef_client.models.credentials_role_request_token_type_role_type import CredentialsRoleRequestTokenTypeRoleType
from ksef_client.ksef_client.models.generate_token_request import GenerateTokenRequest
from ksef_client.ksef_client.models.generate_token_request_type import GenerateTokenRequestType
from ksef_client.ksef_client.api.interfejsy_interaktywne_poswiadczenia import generate_token
from ksef_client.ksef_client.models.generate_token_response import GenerateTokenResponse
from ksef_client.ksef_client.types import Response

def generate_authorization_token(client, session_token):
    
    body = GenerateTokenRequestType(
        description= 'pls generate token xd',
        credentials_role_list= [
            CredentialsRoleRequestTokenType(
                role_type= CredentialsRoleRequestTokenTypeRoleType.INVOICE_WRITE,
                role_description='some role descr'
            )
        ]
    )
    request = GenerateTokenRequest(
        generate_token=body
    )
    
    response: Response[GenerateTokenResponse] = generate_token.sync_detailed(
        client = client,
        json_body=request
    )
    
    return response