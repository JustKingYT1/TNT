import json as j
from abc import ABC, abstractmethod


class Loader(ABC):
    @staticmethod
    @abstractmethod
    def load(file: str):
        pass


class LoaderToJson(Loader):
    @staticmethod
    def load(file):
        with open(file, "r") as read_file:
            return j.load(read_file)
