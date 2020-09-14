class CoffeeCup():
    def _init_(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def fill(self):
        self.amount = self.capacity

    def empty(self):
        self.amount = 0

    def drink(self, amount):
        self.amount -= amount 
        if (self.amount == 0):
            self.amount = 0
            print("Coffee cup is now empty")

adam_cup = CoffeeCup(8)
rome_cup = CoffeeCup(16)
pete_cup = CoffeeCup(12)
taylor_cup = CoffeeCup(2)

rome_cup.fill()
rome_cup.empty()

adam.fill()
adam_cup.drink(8)
print(adam_cup.amount)

pete_cup.fill()
pete_cup.drink(6)
print("Pete has only")