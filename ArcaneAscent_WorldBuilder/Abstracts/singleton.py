"""
Abstract class that prevents any inheriting class from being
constructed more than once.
"""
from abc import ABC, abstractmethod

class Singleton:
    _instance = None

    def __init__(self) -> None:
        raise RuntimeError('Call instance() instead')
    
    @classmethod
    def get(cls):
        return cls._instance
    
    @classmethod
    def instance(cls, *args):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.get().init(*args)
        return cls._instance

    @abstractmethod
    def init(self, *args): pass
    