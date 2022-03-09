from config.consts import ACCEPT, JSON


def get_header(content_type = JSON):
    return {
        'Accept': ACCEPT,
        'content-type': content_type,
    }