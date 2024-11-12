from Bank import Bank
from client import Client
import random


class DSK(Bank):
    NEXT_CLIENT_ID = 1

    def __init__(self, name, amount_of_start_money):
        super().__init__(name, amount_of_start_money)
        self.clients = []
        self.id = Bank.get_next_id()

    def sign_with_next_client(self, client):
        if isinstance(client, Client):
            client.set_id(self._gen_passcode)
            client.set_id(self._get_client_id)
            self.clients.append(client)
            return f"{client.first_name} {client.last_name} signed."

    def _gen_passcode(self):
        passcode = random.randint(1000, 9999)
        return passcode

    def _get_client_id(self):
        current_id = DSK.NEXT_CLIENT_ID
        DSK.NEXT_CLIENT_ID += 1
        return current_id
