import uuid
from logger import logger


class User:
    def __init__(self, username, userpass, email):
        self.id = uuid.uuid4()
        self._username = username
        self._userpass = userpass
        self.email = email
        logger.info(f"An user '{self._username}' was created.")

    @property
    def username(self):
        return self._username

    @property
    def userpass(self):
        return '*' * len(self._userpass)


