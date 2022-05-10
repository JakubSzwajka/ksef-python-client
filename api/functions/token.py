
from base64 import b64encode
from config.consts import PUBLIC_KEY_PATH, TOKEN_INIT_FILE
from ksef_client.ksef_client.api.interfejsy_interaktywne_sesja import init_session_signed, init_session_token
from ksef_client.ksef_client.models.credentials_role_request_token_type import CredentialsRoleRequestTokenType
from ksef_client.ksef_client.models.credentials_role_request_token_type_role_type import CredentialsRoleRequestTokenTypeRoleType
from ksef_client.ksef_client.models.generate_token_request import GenerateTokenRequest
from ksef_client.ksef_client.models.generate_token_request_type import GenerateTokenRequestType
from ksef_client.ksef_client.api.interfejsy_interaktywne_poswiadczenia import generate_token
from ksef_client.ksef_client.models.generate_token_response import GenerateTokenResponse
from ksef_client.ksef_client.models.init_session_response import InitSessionResponse
from ksef_client.ksef_client.models.init_session_signed import InitSessionSignedRequest
from ksef_client.ksef_client.types import Response
from tools.KSeF_xml import KSeF_xml

def generate_authorization_token(client):
    body = GenerateTokenRequestType(
        description= 'pls generate token xd',
        credentials_role_list= [
            CredentialsRoleRequestTokenType(
                role_type= CredentialsRoleRequestTokenTypeRoleType.INVOICE_WRITE,
                role_description='some role descr'
            )
        ]
    )
    
    response: Response[GenerateTokenResponse] = generate_token.sync_detailed(
        client = client,
        json_body=GenerateTokenRequest(
            generate_token=body
        )
    )
    return response


def generate_session_token_init_signed(client, xml_path):
    xml: KSeF_xml = KSeF_xml(xml_path)
    body = InitSessionSignedRequest(bytes=xml.to_bytes())
    response: Response[InitSessionResponse] = init_session_signed.sync_detailed(client=client, request_body=body)
    return response

def generate_session_token_init_token(client, auth_token, challenge_timestamp):
    
    # xml: KSeF_xml = KSeF_xml(TOKEN_INIT_FILE)
    
    token = auth_token + "|" + challenge_timestamp
    token = str.encode(token)

    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding
    
    with open(PUBLIC_KEY_PATH, 'rb') as key_file: 
        public_key = serialization.load_pem_public_key(key_file.read())

    x = public_key.encrypt(
        token,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
            
        )
    )
    print('before encoding')
    print(x)
    x = b64encode(x)
    return x 
