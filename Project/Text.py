from abc import ABC, abstractmethod


class Text(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def show(self):
        pass
