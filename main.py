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


# Helper function to get valid amount from user
def get_valid_amount():
    # Keep asking until we get a valid positive number
    while True:
        try:
            amount = float(input("Amount: $"))
            if amount <= 0:
                print("Amount must be positive! Try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input! Please enter a number.")


# Helper function to show the menu
def display_menu():
    # Show all available options
    print("\n--- Budget Tracker Menu ---")
    print("1) Add income")
    print("2) Add expense")
    print("3) List all transactions")
    print("4) Filter transactions")
    print("5) Show budget summary")
    print("6) Undo last transaction")
    print("0) Exit")


# Function to handle adding income
def handle_add_income(tracker):
    # Get all the information needed for an income transaction
    print("\n--- Add Income ---")
    date = input("Date (YYYY-MM-DD): ")
    amount = get_valid_amount()
    category = input("Category: ")
    description = input("Description: ")
    tracker.add_income(date, amount, category, description)


# Function to handle adding expense
def handle_add_expense(tracker):
    # Get all the information needed for an expense transaction
    print("\n--- Add Expense ---")
    date = input("Date (YYYY-MM-DD): ")
    amount = get_valid_amount()
    category = input("Category: ")
    description = input("Description: ")
    tracker.add_expense(date, amount, category, description)


# Function to handle filtering
def handle_filter(tracker):
    # Let user choose how to filter transactions
    print("\n--- Filter Transactions ---")
    print("1) By type (income/expense)")
    print("2) By category")
    print("3) By month (YYYY-MM)")

    filter_choice = input("Choose filter: ")

    if filter_choice == "1":
        trans_type = input("Type (income/expense): ").lower()
        tracker.filter_transactions("type", trans_type)
    elif filter_choice == "2":
        category = input("Category: ")
        tracker.filter_transactions("category", category)
    elif filter_choice == "3":
        month = input("Month (YYYY-MM): ")
        tracker.filter_transactions("month", month)
    else:
        print("Invalid option!")


# Main function - runs the program
def main():
    # Create the budget tracker
    tracker = BudgetTracker()

    # Welcome message
    print("\n=== Welcome to Budget Tracker Version 1.0 ===")

    # Main loop - keep running until user exits
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            handle_add_income(tracker)
        elif choice == "2":
            handle_add_expense(tracker)
        elif choice == "3":
            tracker.list_transactions()
        elif choice == "4":
            handle_filter(tracker)
        elif choice == "5":
            tracker.show_summary()
        elif choice == "6":
            tracker.undo_last()
        elif choice == "0":
            print("\nThank you for using Budget Tracker!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    main()
