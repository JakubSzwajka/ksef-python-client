from api.consts import CONTENT_TYPE, ACCEPT

def get_header():
    return {
        'Accept': ACCEPT,
        'content-type': CONTENT_TYPE,
    }