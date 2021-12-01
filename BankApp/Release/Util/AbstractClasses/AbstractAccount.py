from abc import abstractmethod, ABC


class AccountInterface(ABC):

    @abstractmethod
    def on_hold(self):
        pass
