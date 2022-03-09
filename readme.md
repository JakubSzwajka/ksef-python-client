
pip install openapi-python-client
Python client for [KSeF](https://ksef-test.mf.gov.pl/)


Tak wygenerowaem cert.pem oraz cert.pfx  ( keys _OLD)
[komentarz na grupie fb](https://www.facebook.com/groups/ksefdevelopers/)
```
openssl req -x509 -days 365 -newkey rsa:2048 -nodes -subj "/2.5.4.42=Jakub /2.5.4.4=Szwajka /2.5.4.5=NIP1111111111" -keyout cert.pem -out cert.pem 
openssl pkcs12 -export -in cert.pem -inkey cert.pem -out cert.pfx
```
hasło: adminadmin



from xml signer doc. KEYS folder
```
openssl req -x509 -sha256 -nodes -subj "/2.5.4.42=Jakub /2.5.4.4=Szwajka /2.5.4.5=NIP1111111111" -days 365 -newkey rsa:2048 -keyout example.key -out example.pem
```


----
To start with KSeF you need to generate certificate with subject fields like in authorization description frame with blue borders form this page https://ksef-test.mf.gov.pl/.
Next to init session you must sign authorization challenge with cert (self signed on test env are granted).
Example with openssl:
openssl req -x509 -new -nodes
/ -subj "/2.5.4.42=Jan /2.5.4.4=Nowak /2.5.4.5=NIP{GENERATED_NIP}"
/ -keyout jan.pk -out jan.cert
Having session token you can grant permission to new person with pesel, nip.
After setting grant for ex. PESEL you need to create new cert including pesel subject field, sign new challenge and start new session.
But now cert generation should have PESEL subject field:
req -x509 -new -nodes -subj "/2.5.4.42=Marek /2.5.4.4=Kowalik /2.5.4.5=PESEL{GENERATED_PESEL}"
Authorization challenge always must be on customer ID -> NIP.
Works on test env 🙂.




openssl req -x509 -new -nodes -subj "/2.5.4.42=Jan /2.5.4.4=Nowak /2.5.4.5=NIP8942908985" -keyout jan.pk -out jan.cert
openssl pkcs12 -export -in jan.cert -inkey jan.pk -out jan.pfx


3385150969

[ req ]
distinguished_name = dn
prompt = no

[ dn ]
CN = Testowa Firma
O = Firma Testowa
C = PL
organizationIdentifier=VATPL-3385150969

openssl req -new -keyout mykey.key -subj '/CN=www.testfirma.pl/O=Testowa firma/C=PL/serialNumber=NIP-1801908070' -out mycsr.csr

'/CN=Jan Kowalski/SN=Kowalski/GN=Jan/O=Testowa firma/C=PL/L=Mazowieckie/serialNumber=NIP-1801908070/description=Jan Kowalski NIP-1801908070'