from src.apilib.util.retry import Retry


class BaseAdapter:
    def  __init__(self):
        pass

    def send(self):
        pass

DEFAULT_RETRY = Retry()

class HTTPAdapter(BaseAdapter):
    def __init__(self, retry: Retry = None):
        super().__init__()
        self.retry = retry or DEFAULT_RETRY

