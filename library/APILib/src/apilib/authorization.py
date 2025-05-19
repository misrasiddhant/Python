import base64


class BaseAuthorization:
    @property
    def __dict__(self):
        return {}

    def header(self):
        raise NotImplementedError


class BasicAuthorization(BaseAuthorization):
    def __init__(self, username:str, password:str):
        self.__username = username
        self.__password = password

    @property
    def username(self):
        return f"{self.__username[:3]}*****" if len(self.__username) > 6 else "*"*len(self.__username)

    def __encoded_credentials(self):
        return base64.b64encode(f"{self.__username}:{self.__password}".encode("utf-8")).decode("utf-8")

    @property
    def header(self):
        return f"Basic {self.__encoded_credentials()}"

