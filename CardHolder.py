class CardHolder:
    def __init__(self, cardnum, pin, firstname, lastname, balance):
        self.cardnum = cardnum
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = float(balance.replace(',', ''))  # Convert balance to float

    # Getter methods

    def get_cardnum(self):
        return self.cardnum

    def get_pin(self):
        return self.pin

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_balance(self):
        return self.balance

    # Setter methods

    def set_cardnum(self, newVal):
        self.cardnum = newVal

    def set_pin(self, newVal):
        self.pin = newVal

    def set_firstname(self, newVal):
        self.firstname = newVal

    def set_lastname(self, newVal):
        self.lastname = newVal

    def set_balance(self, newVal):
        self.balance = float(newVal)  # Ensure balance is always stored as a float

    def print_out(self):
        print("Card #: ", self.cardnum)
        print("pin: ", self.pin)
        print("First Name: ", self.firstname)
        print("Last Name: ", self.lastname)
        print("Balance: ", self.balance)
