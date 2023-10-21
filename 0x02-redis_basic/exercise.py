#!/usr/bin/env python3
"""Create a Cache class"""
import redis
from functools import wraps
import uuid
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """A decorator to count how many times a method was called"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """The wrapper function that store the count"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key_inputs = method.__qualname__ + ":inputs"
        key_outputs = method.__qualname__ + ":outputs"
        self._redis.rpush(key_inputs, str(args))
        outputs = method(self, *args, **kwargs)
        self._redis.rpush(key_outputs, outputs)
        return outputs

    return wrapper


def replay(method: Callable) -> None:
    """display the history of calls of a particular function."""
    my_redis = redis.Redis()
    inputs = my_redis.lrange(method.__qualname__ + ":inputs", 0, -1)
    outputs = my_redis.lrange(method.__qualname__ + ":outputs", 0, -1)
    inp_out = zip(inputs, outputs)
    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for inp, out in inp_out:
        print(f"{method.__qualname__}(*{inp.decode('utf-8')}) -> "
              f"{out.decode('utf-8')}")


class Cache:
    """Stores a cache data."""

    def __init__(self) -> None:
        """Initialize the redis database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store a data with a random key
        :param data: data to be stored
        :return: tha random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
        str, bytes, int, float]:
        """
        Gets the value of a key
        :param key: string key
        :param fn: callable function used to convert the value to its
        original format
        :return: the original value
        """

        if fn is None:
            return self._redis.get(key)
        else:
            return fn(self._redis.get(key))

    def get_int(self, data: bytes) -> int:
        """Convert data to int"""
        return int(data)

    def get_str(self, data: bytes) -> str:
        """Convert data to str"""
        return data.decode('utf-8')
