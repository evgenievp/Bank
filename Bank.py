from abc import ABC, abstractmethod
import random

from client import Client


class Bank(ABC):
    NEXT_ID = 1
    NEXT_CLIENT_ID = 1

    def __init__(self, name, amount_of_start_money):
        self.name = name
        self.__amount_of_money = amount_of_start_money
        self.clients = []

    @classmethod
    def get_next_id(cls):
        current_id = Bank.NEXT_ID
        cls.NEXT_ID += 1
        return current_id

    @abstractmethod
    def sign_with_next_client(self, first_name, last_name):
        pass

    @abstractmethod
    def _gen_passcode(self):
        pass

    @abstractmethod
    def _get_client_id(cls):
        pass
