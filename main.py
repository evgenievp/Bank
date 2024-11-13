from DSK import DSK
from ProCredit import ProCredit
from client import Client


bank_dsk = DSK("DSK Bank")
pro_credit = ProCredit("Pro Credit Bank")
pesho = Client("Petar", "ivanov")
gosho = Client("Georgi", 'Ivanov')

bank_dsk.sign_with_next_client(pesho)
bank_dsk.sign_with_next_client(gosho)

print(gosho.bank)
print(pesho.bank)
print(pesho.get_passcode())
print(gosho.get_passcode())
print("-" * 20)
print(gosho.deposit(1000, gosho.get_passcode()))
print(pesho.deposit(1000, pesho.get_passcode()))
print("-" * 20)
gosho.change_bank(pro_credit)
pro_credit.sign_with_next_client(gosho)
gosho.deposit(gosho.money, gosho.get_passcode())
print(gosho.bank)
print(gosho.withdraw(100, gosho.get_passcode()))
print(gosho.check_balance(gosho.get_passcode()))

