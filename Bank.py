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
        client = Client(first_name, last_name, self.__gen_passcode, self.__get_client_id)
        self.clients.append(client)

    @abstractmethod
    def __gen_passcode(self):
        passcode = random.randint(1000, 9999)
        return passcode

    def __get_client_id(cls):
        current_id = Bank.NEXT_CLIENT_ID
        cls.NEXT_CLIENT_ID += 1
        return current_id
