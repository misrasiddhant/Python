from enum import Enum
from typing import Callable

ALLOWED_METHODS = frozenset(["HEAD", "GET", "PUT", "DELETE", "OPTIONS", "TRACE"])
RETRY_FOR_STATUS = frozenset([413, 429, 503])

class RetryMode(Enum, str):
    FIXED = "fixed"
    BACKOFF = "backoff"

class Retry:
    def __init__(
            self,
            mode: RetryMode = RetryMode.FIXED,
            num_retries:int = 0,
            allowed_methods: set[str] | None = ALLOWED_METHODS,
            retry_for_status: set[int] | None = RETRY_FOR_STATUS,
            backoff: float = 0,
            backoff_jitter: float = 0
    ) -> None:
        self.mode = mode,
        self.num_retries = num_retries
        self.allowed_methods = allowed_methods
        self.retry_for_status = retry_for_status
        self.backoff = backoff
        self.backoff_jitter = backoff_jitter

    def retry(self, request):
        retry_count = 0

        while retry_count <= self.num_retries:
            response = request()
            if response.status_code not in self.retry_for_status:
                return response


        pass
