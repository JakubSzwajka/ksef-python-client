

class KSeF_signer:
    pass 
    # KEYS_ROOT = 'keys/'
    # KEY = 'example.key'
    # CERT = 'example.pem'
    
    # def __init__(self, key_path, cert_path) -> None:
    #     with open(key_path) as f:
    #         self.key = f.read()
            
    #     with open(cert_path) as f:
    #         self.cert = f.read()
        
    # def sign(self, xml_root):
    #     signed_root = XMLSigner(
    #             # method=methods.enveloping,
    #             c14n_algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315'
    #             # c14n_algorithm='http://www.w3.org/2000/09/xmldsig#base64'
    #         ).sign(
    #         xml_root, 
    #         key=self.key, 
    #         cert=self.cert,
    #         always_add_key_value=True, # to dodaje KeyInfo -> KeyValue
    #         # payload_inclusive_ns_prefixes = {'test'}
    #         passphrase=b'admin'
    #         )
    #     return signed_root
    
    # def verify(self, xml_root):
    #     verified_data = XMLVerifier().verify(
    #         xml_root,
    #         x509_cert=self.cert
    #         ).signed_xml
    #     return verified_data
