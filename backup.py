# Standard modules.
from pathlib import Path
from typing import NamedTuple
from logging import getLogger, setLoggerClass

# Custom modules.
from logger import CustomLogger


class Version(NamedTuple):
    major: int
    minor: int
    patch: int

    def __str__(self):
        return f'{self.major}.{self.minor}.{self.patch}'

class TodoistBackup():
    version = Version(0, 0, 1)
    config_dir = Path(__file__).parents[0] / 'config'
    config_dir.mkdir(exist_ok=True)  # create 'config' folder if it doesn't exist.
    _env_var_name = 'TOKEN'
    _token_file_path = config_dir / 'todoist_token.env'

    def __init__(self, token=None):
        self._token = None

        if token is not None:
            # Use the setter validation if a token is provided at init.
            self.token = token

        setLoggerClass(CustomLogger)
        self.logger = getLogger(__name__)

    @property
    def token(self) -> str:
        return self._token

    @token.setter
    def token(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError('Token must be a non-empty string.')
        self._token = value.strip()

    def set_token(self, new_value: str) -> None:
        if new_value is None:
            self.logger.error('Token value cannot be empty.')
            return None
        else:
            with open(self._token_file_path, 'w+') as file:
                file.write(f'TOKEN={new_value}')
