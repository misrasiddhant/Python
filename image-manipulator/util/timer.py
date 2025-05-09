import functools
import logging
import time
from functools import lru_cache

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@lru_cache
class Timer(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.start_time = time.perf_counter()
        return self.func(*args, **kwargs)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.start_time:
            duration = self.start_time - time.perf_counter()
            logger.info(f"Operation took {duration * 1000} ms")


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        return_value = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        logger.info(f"Operation {func.__name__} took {duration*1000:.2f} ms")
        return return_value

    return wrapper_timer
