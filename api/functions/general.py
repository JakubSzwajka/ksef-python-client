from ksef_client.ksef_client.client import Client
from tools.KSeF_xml import KSeF_xml
from datetime import datetime
import ast

def save_signed(
    xml: KSeF_xml, 
    name = f'signed_{int(datetime.timestamp(datetime.now( )))}.xml', 
    folder = '/Users/jakubszwajka/Desktop/to_sign/'):
        
    with open( name, 'w') as f: 
        f.write(xml.to_string())
    
def get_response_data(response, print_data = True):
    try:
        response_data = ast.literal_eval(response.content.decode('UTF-8'))     
        if print_data:
            print(response_data)
    except (ValueError, AttributeError)as e:
        print(e)
        print('----------')
        print(response)
        return response 
    return response_data

def create_client(url, header):
    return Client(base_url=url, headers=header)
