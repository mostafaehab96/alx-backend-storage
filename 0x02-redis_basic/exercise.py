#!/usr/bin/env python3
"""Create a Cache class"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """Stores a cache data."""

    def __init__(self):
        """Initialize the redis database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, int, bytes]) -> str:
        """
        Store a data with a random key
        :param data: data to be stored
        :return: tha random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Callable[[str], Union[str, int, float,
    bytes]] = None) -> Union[str, int, float, bytes]:
        """
        Gets the value of a key
        :param key: string key
        :param fn: callable function used to convert the value to it's
        original format
        :return: the original value
        """

        if fn is None:
            return self._redis.get(key)
        else:
            return fn(self._redis.get(key))
