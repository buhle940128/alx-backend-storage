import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """Initialize Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.
        
        Args:
            data: The data to store (str, bytes, int, or float)

        Returns:
            str: The key under which the data is stored
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
