#!/usr/bin/env python3
"""Create a Cache class"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Stores a cache data."""

    def __init__(self) -> None:
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
