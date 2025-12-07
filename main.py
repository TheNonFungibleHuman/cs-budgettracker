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
