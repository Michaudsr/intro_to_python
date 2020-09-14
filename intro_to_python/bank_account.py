class BankAccount():
    def __init__(self, kind, pin):
        self.kind = kind
        self.balance = 0
        self.overdraft_fees = 0
        self.pin = pin
    
    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount, pin_from_user):

        if (self.pin == pin_from_user):
            if (self.balance < amount):
                print("Sorry, you don't have that amount in your account.")
                return
            elif (self.balance == amount):
                self.balance -= amount
                print("You are now empty my friend AKA you're broke.")
                return
            else:
                self.balance -= amount
                print("Current balance is now {}".format(self.balance))
                return 
        else:
            print("The pin number is incorrect. Please try again")
        # if (self.balance < 0):
        #     self.overdraft_fees += 36
        # return amount

    def change_pin(self, pin):
        self.pin = pin
        print(f"The new pin number is {self.pin}")


rome_checking = BankAccount("checking", 1234)
print("My new account is a {} account".format(rome_checking.kind))

rome_checking.deposit(3000)
# print("My current balance is ${}.".format(rome_checking.balance))

rome_checking.withdraw(1500, 1555)
# print("My current balance is ${}.".format(rome_checking.balance))

rome_checking.withdraw(2000, 1234)
# print("My overdraft fee is currently {}".format(rome_checking.overdraft_fees))
# print("My current balance is ${}.".format(rome_checking.balance))

rome_checking.change_pin(9987)