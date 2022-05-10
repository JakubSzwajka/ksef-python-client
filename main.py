
from api.functions.general import create_client, get_response_data
from api.functions.token import generate_authorization_token, generate_session_token_init_signed, generate_session_token_init_token
from config.consts import  SIGN_INIT_FILE, TEST_ENDPOINT_URL, XML_SAMPLES_ROOT

from api.functions import authorization_challange_call, set_challenge, save_signed

from ksef_client.ksef_client.models.init_session_signed import InitSessionSignedRequest 
from ksef_client.ksef_client.api.interfejsy_interaktywne_sesja import init_session_signed
from ksef_client.ksef_client.models.init_session_response import InitSessionResponse
from ksef_client.ksef_client.types import Response

from tools.KSeF_xml import KSeF_xml
from tools.utils import get_header
import click

# IDENTIFIER = '5250001090'
FUNCTIONS = ['challenge', 'set_challenge', 'session_token', 'generate_token']

@click.command()
@click.argument('func',required=True, type=click.Choice(FUNCTIONS))
@click.option('--identifier', type=int, help='Identifier - nip - 10 digit')
@click.option('--xml_path', default=None, help='Path to xml to be send or save')
@click.option('--challenge', default=None, help='Challenge to be set')
@click.option('--token', default=None, help='Session token')
@click.option('--auth_token', default=None, help='Authorization token')
@click.option('--challenge_timestamp', default=None, help='Challenge timestamp')
def main(identifier, func, challenge, xml_path, token, auth_token, challenge_timestamp):
    
    client = create_client(TEST_ENDPOINT_URL, header=get_header(token=token))
    
    if func == 'challenge':
        assert identifier != None, "Please specify identifier to generate challenge"
        response = authorization_challange_call(client, identifier)
        r_data = get_response_data(response)
        
        ch = r_data.get('timestamp')
        from datetime import datetime
        import pytz
        from time import gmtime
        utc_datetime = datetime.utcnow()
        # ch = '2022-03-24T17:22:05.420Z'
        dt_obj = datetime.strptime(ch,'%Y-%m-%dT%H:%M:%S.%fZ')
        dt_obj = dt_obj.replace(microsecond=0)
        millisec = dt_obj.timestamp() * 1000
        millisec += 3600000
        print(f'Miliseconds: {millisec}')
        
        print(dt_obj.tzinfo)
        print(dt_obj)

        
        
        return
    
    if func == 'set_challenge':
        assert challenge != None, "Please provide challenge to be set"
        assert xml_path != None, "Please provide xml_path where file should be saved"
        xml: KSeF_xml = KSeF_xml(XML_SAMPLES_ROOT + SIGN_INIT_FILE)
        xml = set_challenge(xml, challenge)
        save_signed(xml, xml_path)
        return
    
    if func == 'session_token':
        assert xml_path != None or auth_token != None, "Please provide xml_path with signed file to be send or authorization token"
        assert not ( xml_path != None and auth_token !=None ), "Choose one method to obtain session token. xml for initSigned or auth token for initToken"
        
        if xml_path:
            response = generate_session_token_init_signed(client, xml_path)
        if auth_token:
            assert challenge_timestamp != None, "To generate session token with InitToken, provide timestamp"
            response = generate_session_token_init_token(client, auth_token, challenge_timestamp)
        r_data = get_response_data(response)
        return
    
    if func == 'generate_token':
        assert token != None, "Please provide session token"
        response = generate_authorization_token(client)
        r_data = get_response_data(response)
        return
                
    raise Exception('which func. should i run? xd')

if __name__ == '__main__':
    main( )
    