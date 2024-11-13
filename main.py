from DSK import DSK
from client import Client

pesho = Client("Petar", "ivanov")
bank_dsk = DSK("DSK Bank")
bank_dsk.sign_with_next_client(pesho)

print(pesho.bank)
print(pesho.deposit(1000, pesho.get_passcode()))
print(pesho.remove_bank_account())

