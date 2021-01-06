from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def move(self):
        pass
