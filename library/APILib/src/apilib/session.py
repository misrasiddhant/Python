from urllib3 import request

from src.apilib.adapters import HTTPAdapter, BaseAdapter


class Session:
    def __init__(
            self,
            auth = None,
            adapter: BaseAdapter = HTTPAdapter(),
            verify:bool = False
        ):
        self.auth = auth
        self.verify = verify
        self.adapter = adapter

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    def get(self, url: str, query_parameters = None):
        response = request(
            method = "GET",
            url= url
        )