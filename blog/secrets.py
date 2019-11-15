import json
import os
import sys
from typing import Optional, List

_SECRETS_FILE = 'secrets.txt'
_PUBLIC_KEY_ENV = 'PLAID_PUBLIC_KEY'
_CLIENT_ID_ENV = 'PLAID_CLIENT_ID'
_SECRET_ENV = 'PLAID_SECRET'


class Secrets:
    def __init__(self):
        self.public_key = os.getenv(_PUBLIC_KEY_ENV)  # type: Optional[str]
        self.client_id = os.getenv(_CLIENT_ID_ENV)  # type: Optional[str]
        self.secret = os.getenv(_SECRET_ENV)  # type: Optional[str]
        self._check_secrets()

        self._access_tokens = []  # type: List[str]

        self._read_access_tokens()

    @property
    def access_tokens(self) -> List[str]:
        return self._access_tokens

    @access_tokens.setter
    def access_tokens(self, value: List[str]):
        self._access_tokens = value
        self._write_access_tokens()

    def _write_access_tokens(self) -> None:
        with open(_SECRETS_FILE, 'w') as f:
            json.dump({'access_tokens': self._access_tokens}, f)

    def _read_access_tokens(self) -> None:
        try:
            with open(_SECRETS_FILE) as f:
                info = json.load(f)
                self._access_tokens = info['access_tokens']
        except FileNotFoundError:
            pass

    def _check_secrets(self) -> None:
        if not (self.public_key and self.client_id and self.secret):
            print(f'ERROR: each of the {_CLIENT_ID_ENV}, {_PUBLIC_KEY_ENV}, and {_SECRET_ENV} '
                  'environment variables must be set properly')
            sys.exit(1)