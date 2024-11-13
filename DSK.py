from Bank import Bank
from client import Client
import random


class DSK(Bank):
    NEXT_CLIENT_ID = 1
    MONEY = 1_000_000

    def __init__(self, name):
        super().__init__(name)
        self.interest = 0.05
        self.clients = []
        self.id = self._get_next_id()

    def sign_with_next_client(self, client):
        if isinstance(client, Client):
            client.set_passcode(self._gen_passcode())
            client.set_id(self._get_client_id)
            client.bank = self.__class__
            self.clients.append(client)
            return f"{client.first_name} {client.last_name} signed."

    def _gen_passcode(self):
        passcode = random.randint(1000, 9999)
        return str(passcode)

    def _get_client_id(self):
        current_id = DSK.NEXT_CLIENT_ID
        DSK.NEXT_CLIENT_ID += 1
        return current_id

    @classmethod
    def deposit(cls, amount):
        DSK.MONEY += amount

    def withdraw(cls, amount):
        DSK.MONEY -= amount

    def _get_next_id(self):
        current_id = DSK.NEXT_ID
        DSK.NEXT_ID += 1
        return current_id

    def remove_client(self, client):
        for client in self.clients:
            if client == client.last_name:
                client.remove_bank_account()
                self.clients.remove(client)
                return f"Sorry to see you go, {client.first_name} {client.last_name}"
        return f"We haven't client with that last name in our database."

    def __repr__(self):
        return __class__.__name__
