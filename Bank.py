from abc import ABC, abstractmethod


class Bank(ABC):
    NEXT_ID = 1
    NEXT_CLIENT_ID = 1

    def __init__(self, name):
        self.name = name
        self.clients = []

    @abstractmethod
    def _get_next_id(self):
        pass

    @abstractmethod
    def sign_with_next_client(self, client):
        pass

    @abstractmethod
    def _gen_passcode(self):
        pass

    @abstractmethod
    def _get_client_id(self):
        pass


