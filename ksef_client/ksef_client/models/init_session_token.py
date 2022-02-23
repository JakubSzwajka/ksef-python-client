import pathlib
from typing import Any, Dict, List, Type, TypeVar

from api.consts import TOKEN_INIT_FILE

import re

class InitSessionTokenRequest:
    """
    Attributes: 
        path
    """


    def __init__(self, path, challenge) -> None:
        self.challenge = challenge
        self.bytes_data = None
        self.content = None

        if path:
            self.path = path
        else: 
            self.path = TOKEN_INIT_FILE

        self._read_file()
        self._update_challenge()
    
    def _read_file(self):
        with open(self.path, 'r') as f: 
            self.content = f.read( )
            # f.seek(0)
            # updated_file = re.sub('<Challenge>[\s\S]*?<\/Challenge>', f'<Challenge>{self.challenge}</Challenge>', file)
            # f.write(updated_file)


    def _update_challenge(self):
        self.content = re.sub('<Challenge>[\s\S]*?<\/Challenge>', f'<Challenge>{self.challenge}</Challenge>', self.content)
        if self.content:
            print(f'File {self.path}, updated with challenge {self.challenge}')


    @property
    def bytes(self):
        return self.content.encode('UTF-8')
    