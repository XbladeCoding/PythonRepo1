class chip:
    def __init__(self, money, stock):
        self.money = money
        self.stock = stock
    def eatChip(self):
        print('The chip has been eaten.')
    def buyChip(self):
        if (price > self.money):
            print('You do not have enough money to buy chips :(')
            return 0
        if (self.stock <= 0):
            print('There are no more chips left.')
            return 0
        self.money = self.money-price
        self.stock = self.stock-1
        print('The chip has been bought.')
        return 1
money = float(input('How much money do you have?'))
stock = float(input('The stock of chips is what?'))
price = 3.99

chip1 = chip(money, stock)
chipsBought = 0
# keep buying chips until you have money
while (chip1.buyChip() == 1):
   chip1.eatChip()
   chipsBought += 1

print('You have ' + str(round(chip1.money, 2)) + ' dollars left.')
print('There are ' + str(chip1.stock) + ' chips left.')
print('You bought ' + str(chipsBought) + ' chips.')
# print how much money left and how many chips left