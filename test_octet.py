import requests
import ast 
from pprint import pprint

with open('./api/xml_samples/token.xml', 'rb') as f:
    data = f.read()
res = requests.post(url='https://ksef-test.mf.gov.pl/api/online/Session/InitToken',
                    data=data,
                    headers={'Content-Type': 'application/octet-stream'})

print(res.status_code)
response_data = ast.literal_eval(res.content.decode('UTF-8')) 
pprint(response_data)