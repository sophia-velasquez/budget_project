class Budget:
    amount = 0

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # METHODS
    def deposit(self, amount):
        self.amount += amount
        return "You have deposited ${} to the {} category.".format(amount, self.category)

    def view_balance(self, category):
        return "The current balance for {} category is: ${}.".format(category.category, self.amount)

    def check_balance(self, amount):
        # Checks if the amount is less or greater than the self.amount
        if self.amount > amount:
            return "You have more than ${} in the {} category.".format(amount, self.category)
        elif self.amount == amount:
            return "You have exactly ${} in the {} category.".format(amount, self.category)
        else:
            return"You have less than ${} in the {} category.".format(amount, self.category)

    def withdraw(self, amount):
        if self.amount >= amount:
            self.amount -= amount
            return "You have withdrawn ${} from the {} category.".format(amount, self.category)
        else:
            return "Insufficient funds available."

    def transfer(self, amount, category):
        # Transfer money between one category (e.g. food) to another (e.g. clothes)
        if self.amount >= amount:
            print("The current balance in %s is $%d." % (self.category, self.amount))
            self.amount -= amount
            category.deposit(amount)
            print("Transferring $%d from the %s category to the %s category..." % (
                amount, self.category, category.category))
            print("The new balance in %s is $%d." % (category.category, category.amount))
            return "The new balance in {} is ${}.".format(self.category, self.amount)
        else:
            return "Insufficient funds available in the {} category.".format(self.category)


category_food = Budget("Food", 500)
category_clothes = Budget("Clothing", 300)
category_car = Budget("Car", 300)
category_ent = Budget("Entertainment", 150)

# EXAMPLE COMMANDS

print("/// Transfer money from Entertainment to Food ///")
print(category_ent.transfer(50, category_food))

print("/// View balance for Car ///")
print(category_car.view_balance(category_car))

print("/// Check balance for Clothing in relation to $500 ///")
print(category_clothes.check_balance(500))

print("/// Withdraw money from Food ///")
print(category_food.withdraw(550))
print(category_food.view_balance(category_food))

print("/// Deposit money to Food ///")
print(category_food.deposit(250))
print(category_food.view_balance(category_food))
