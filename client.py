class Client:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__balance = 0
        self.__wrong_passcodes = 0
        self.__passcode = None
        self.__id = None
        self.bank = None

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if value.strip() == "" or len(value) < 2:
            raise ValueError("Can't have name with only white spaces or lower than two characters.")
        else:
            self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if value.strip() == "" or len(value) < 3:
            raise ValueError("Can't have last name with only white spaces or lower than three characters.")
        else:
            self.__last_name = value

    def withdraw(self, amount, passcode):
        if passcode != self.__passcode:
            return "Sorry. Wrong passcode"
        if self.bank.amount_of_money < amount:
            return f"Sorry. {self.bank} can't provide amount of {amount:.2f$}."
        if amount > self.__balance:
            return "Impossible transaction. Not enough money! Please contact bank Support."
        else:
            self.__balance -= amount
            self.__balance -= amount
            return f"Successful withdraw of {amount:.2f}$. Current balance: {self.__balance:.2f}$."

    def deposit(self, amount, passcode):
        if passcode != self.__passcode:
            return "Sorry. Wrong passcode."
        self.__balance += amount
        self.bank.amount_of_money += amount
        return f"Successful deposit of {amount:.2f}"

    def check_balance(self, passcode):
        if self.__passcode != passcode:
            if not self.__wrong_checks():
                return "Sorry. Wrong passcode."
            else:
                return f"Current balance: {self.__balance:.2f$}"

    def __wrong_checks(self):
        self.__wrong_passcodes -= 1
        if self.__wrong_passcodes == 0:
            print("This card is now locke due three wrong passcodes.")
            return False
        return True

    def set_bank(self, bank):
        self.bank = bank
        return "Sign successful"

    def set_id(self, id):
        self.__id = id

    def set_passcode(self, passcode):
        self.__passcode = passcode