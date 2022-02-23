from api.consts import ACCEPT, JSON, XML_SAMPLES_ROOT
import xml.etree.ElementTree as ET
import re 
import pathlib

def get_header(content_type = JSON):
    return {
        'Accept': ACCEPT,
        'content-type': content_type,
    }

def get_xml(name):
    ET.register_namespace('','http://ksef.mf.gov.pl/schema/gtw/svc/online/types/2021/10/01/0001')
    ET.register_namespace('','http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001')
    ET.register_namespace('','http://ksef.mf.gov.pl/schema/gtw/svc/online/auth/request/2021/10/01/0001')
    xml_tree = ET.parse(f'{XML_SAMPLES_ROOT}{name}')
    return xml_tree

def update_challenge(file_name, challenge):
    path = str(pathlib.Path(__file__).parent.resolve()) + '/xml_samples/' + file_name
    with open(path, 'r+') as f: 
        file = f.read( )
        f.seek(0)
        updated_file = re.sub('<Challenge>[\s\S]*?<\/Challenge>', f'<Challenge>{challenge}</Challenge>', file)
        f.write(updated_file)

    print(f'File {file_name}, updated with challenge {challenge}')

