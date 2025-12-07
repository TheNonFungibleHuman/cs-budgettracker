app_name = " Budget Tracker"
version = " 1.0"
print("Welcome to" +app_name+version)


class Transaction:

    def __init__(self, date, amount, category, description, ttype):
        # Initialize a transaction with basic information
        # date: when the transaction happened (string)
        # amount: how much money (will convert to float)
        # category: what type of spending/income (like 'food', 'salary')
        # description: brief note about the transaction
        # ttype: either 'income' or 'expense'

        self.date = date
        self.amount = float(amount)  # Convert to number
        self.category = category.lower().strip()  # Make lowercase and remove extra spaces
        self.description = description
        self.type = ttype

    def display(self):
        # Show the transaction information
        if self.type == "income":
            symbol = "+"
        else:
            symbol = "-"

        print(
            "[" + self.date + "] " + symbol + "$" + str(self.amount) + " | " + self.category + " | " + self.description)


# Income class inherits from Transaction
class Income(Transaction):

    def __init__(self, date, amount, category, description):
        # Create an income transaction
        # Automatically sets type to 'income'
        super().__init__(date, amount, category, description, "income")


# Expense class inherits from Transaction
class Expense(Transaction):

    def __init__(self, date, amount, category, description):
        # Create an expense transaction
        # Automatically sets type to 'expense'
        super().__init__(date, amount, category, description, "expense")

    def check_warning(self, threshold):
        # Warn if expense is above threshold (budget threshold warning feature)
        if self.amount > threshold:
            print("Warning: Large expense of $" + str(self.amount) + "!")