from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def create_address(self):
        pass
