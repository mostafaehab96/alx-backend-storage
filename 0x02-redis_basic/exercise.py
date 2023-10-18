#!/usr/bin/env python3
"""Create a Cache class"""
import redis
import uuid
from typing import Union


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
