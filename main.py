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


# Main BudgetTracker class - manages all transactions
class BudgetTracker:

    def __init__(self):
        # Start with an empty list of transactions
        self.transactions = []

    def add_income(self, date, amount, category, description):
        # Add a new income transaction
        income = Income(date, amount, category, description)
        self.transactions.append(income)
        print("Income added: $" + str(amount))

    def add_expense(self, date, amount, category, description):
        # Add a new expense transaction
        expense = Expense(date, amount, category, description)
        self.transactions.append(expense)
        print("Expense added: $" + str(amount))
        # Budget threshold warning - warn if expense is large
        expense.check_warning(1000)

    def list_transactions(self):
        # Show all transactions
        if not self.transactions:
            print("No transactions yet.")
            return

        print("\n=== All Transactions ===")
        for trans in self.transactions:
            trans.display()

    def filter_transactions(self, filter_type, filter_value):
        # Filter and show transactions based on type, category, or month
        filtered = []

        # Go through each transaction and check if it matches the filter
        for trans in self.transactions:
            if filter_type == "type" and trans.type == filter_value:
                filtered.append(trans)
            elif filter_type == "category" and trans.category == filter_value.lower():
                filtered.append(trans)
            elif filter_type == "month" and trans.date.startswith(filter_value):
                filtered.append(trans)

        # Show results
        if not filtered:
            print("No transactions found for " + filter_type + ": " + filter_value)
            return

        print("\n=== Filtered Transactions ===")
        for trans in filtered:
            trans.display()

    def show_summary(self):
        # Display budget summary with totals and balance
        if not self.transactions:
            print("No transactions to summarize.")
            return

        # Calculate total income
        total_income = 0
        for trans in self.transactions:
            if trans.type == "income":
                total_income += trans.amount

        # Calculate total expenses
        total_expense = 0
        for trans in self.transactions:
            if trans.type == "expense":
                total_expense += trans.amount

        # Calculate balance
        balance = total_income - total_expense

        # Calculate spending by category
        categories = {}
        for trans in self.transactions:
            if trans.category not in categories:
                categories[trans.category] = 0
            categories[trans.category] += trans.amount

        # Display summary
        print("\n=== Budget Summary ===")
        print("Total Income:   $" + str(total_income))
        print("Total Expenses: $" + str(total_expense))
        print("Balance:        $" + str(balance))
        print("\n=== By Category ===")
        for cat in categories:
            print(cat + ": $" + str(categories[cat]))

    def undo_last(self):
        # Undo last transaction - removes the most recent one
        if not self.transactions:
            print("No transactions to undo.")
            return

        # Get the last transaction before removing it
        last_trans = self.transactions[-1]
        self.transactions.pop()
        print("Undid last transaction: " + last_trans.type + " of $" + str(last_trans.amount))