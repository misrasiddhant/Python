from enum import Enum
from http.client import HTTPConnection
from typing import Dict, Literal


class Method(str, Enum):
    HEAD = "HEAD"
    OPTION = "OPTION"
    GET = "GET"
    POST = "POST"
    PUT = "PUT"

class ContentType(Enum):
    TEXT_PLAIN = 'text/plain'
    TEXT_HTML = 'text/html'
    APPLICATION_JSON = 'application/json'
    APPLICATION_XML = 'application/xml'
    IMAGE_JPEG = 'image/jpeg'
    IMAGE_PNG = 'image/png'
    IMAGE_GIF = 'image/gif'
    AUDIO_MPEG = 'audio/mpeg'
    VIDEO_MP4 = 'video/mp4'
    APPLICATION_OCTET_STREAM = 'application/octet-stream'

class Endpoint:
    protocol: Literal['https', 'http']
    hostname: str
    port: int
    path: str

    def __init__(self, protocol, hostname, port, path):
        self.protocol = protocol
        self.hostname = hostname
        self.port = port
        self.path = path

    def __repr__(self):
        return "  ".join(f"{key}={value}" for key, value in self.__dict__.items())


class Request:
    def __init__(self):
        self.method = None
        self.url = None
        self.query_string = {}
        self.header = {}
        self.body = {}
        self.auth = None
        self.verify_ssl = True

    @staticmethod
    def _parse_endpoint(url:str, query_string: Dict[str, str] = None) -> Endpoint:

        scheme = "http" # default scheme
        _url = url
        try:
            scheme, _url = url.split("://")
        except Exception:
            #Log warning that default scheme `http` will be used.
            pass

        _url_split = _url.split("/")
        hostname, port = _url_split[0].split(":")
        path = "/".join(_url_split[1:])

        #ToDo: Validate and set url

        if query_string:
            for key, value in query_string.items():
                path += f"&{key}={value}"

        return Endpoint(scheme.lower(), hostname, port, path)

    @staticmethod
    def _prepare_body(body:[str|dict]) -> (ContentType, str):
        """
        #ToDo:
         - Form Data
         - Raw (Text, JS, JSON, HTML, XML) -> Set headers accordingly
         - Binary
         - GraphQL
        :param body:
        :param json:
        :return:
        """
        if isinstance(body, dict):
            return ContentType.APPLICATION_JSON, body
        return None, None
        raise NotImplementedError

    @staticmethod
    def request(endpoint:Endpoint, method: Method, headers: dict):
        connection = HTTPConnection(
            host=endpoint.hostname,
            port=endpoint.port
        )
        try:
            if headers:
                for key, value in headers.values():
                    connection.putheader(key, value)
            connection.putrequest(method=method, url=endpoint.path)
            response = connection.getresponse()
            return response
        except Exception as e:
            raise e
        finally:
            connection.close()



    def get(self, url:str, query_string: Dict[str, str] = None):
        self.method = Method.GET
        endpoint = self._parse_endpoint(url, query_string)
        # self.body = self._prepare_body()
        headers = {}

        return self.request(endpoint, Method.GET, headers)



print(Request()._parse_endpoint("http://www.example.com:9090/test",{"key": "234", "key2": "567"}))
print(Request().get("http://www.example.com:9090/test"))