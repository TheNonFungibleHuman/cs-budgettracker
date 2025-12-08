# 🧾 Budget Tracker

A command-line application developed in **Python 3** as part of the **Programming 1 Formative Project (Week 7)**.  
This tool enables users to track their finances by recording income and expenses, viewing transactions, filtering them, and generating summaries—all within a single terminal session.  

Data is stored **in memory only** (no file persistence).

---

## 📌 Project Overview

The application demonstrates key Python concepts:

- **Strings & Conditionals** → Menu navigation and validation  
- **Loops** → Iteration over transactions  
- **Functions** → Modularity and reusability  
- **Collections** → Lists and dictionaries for data storage  
- **Object-Oriented Programming (OOP)** →  
  - `Transaction` base class  
  - `BudgetTracker` manager class  
  - Inheritance via `Income` and `Expense` subclasses  

---

## ✨ Features

- **Add Transactions** → Add income or expense entries with date (`YYYY-MM-DD`), amount, category, and description.  
- **List Transactions** → Display all transactions in a readable format.  
- **Filter Transactions** → Filter by type (income/expense), category, or month (`YYYY-MM`).  
- **Summarize Budget** → Show total income, total expenses, balance, and category-wise totals.  
- **Input Validation** → Handles invalid inputs gracefully.  

### 🔧 Optional Features Implemented
- Budget threshold warnings for expenses over **$1000**  
- Undo last transaction  

---

## ▶️ Instructions to Run

1. Ensure **Python 3** is installed on your system.  
2. Clone the repository:

   ```bash
   git clone https://github.com/TheNonFungibleHuman/cs-budgettracker.git
3. Navigate to the project directory:
   ```bash
   cd cs-budgettracker
4. Run the script:
   ```bash
   python main.py
5. Interact via the menu; enter 0 to exit.

  No external libraries are required.

## 📋 Menu Structure

    --- Budget Tracker Menu ---
    1) Add income
    2) Add expense
    3) List all transactions
    4) Filter transactions
    5) Show budget summary
    6) Undo last transaction
    0) Exit

### For option 4 (Filter transactions), a sub-menu is shown:

    --- Filter Transactions ---
    1) By type (income/expense)
    2) By category
    3) By month (YYYY-MM)

## 💻 Sample Interactions

### Adding Income

    Enter your choice: 1
    
    --- Add Income ---
    Date (YYYY-MM-DD): 2025-12-01
    Amount: $2500
    Category: Freelance
    Description: Project payment
    Income added: $2500

### Adding Expense (Triggering Warning)

    Enter your choice: 2
    
    --- Add Expense ---
    Date (YYYY-MM-DD): 2025-12-03
    Amount: $1500
    Category: Travel
    Description: Flight tickets
    Expense added: $1500
    Warning: Large expense of $1500!

### Listing Transactions

    Enter your choice: 3
    
    === All Transactions ===
    [2025-12-01] +$2500.0 | freelance | Project payment
    [2025-12-03] -$1500.0 | travel   | Flight tickets

### Filtering by Month

    Enter your choice: 4
    
    --- Filter Transactions ---
    Choose filter: 3
    Month (YYYY-MM): 2025-12

    === Filtered Transactions ===
    [2025-12-01] +$2500.0 | freelance | Project payment
    [2025-12-03] -$1500.0 | travel   | Flight tickets

### Showing Summary

    Enter your choice: 5
    
    === Budget Summary ===
    Total Income: $2500.0
    Total Expenses: $1500.0
    Balance: $1000.0
    
    === By Category ===
    freelance: $2500.0
    travel: $1500.0

### Undoing Last Transaction

    Enter your choice: 6 Undid last transaction: expense of $1500.0
    
## Working Screenshots
<img width="1315" height="364" alt="image" src="https://github.com/user-attachments/assets/aee6ffb6-16f1-45be-984c-b095250226fe" />

<img width="330" height="191" alt="image" src="https://github.com/user-attachments/assets/0672bda8-5165-4156-bc02-6b4bab9d1051" />

<img width="473" height="456" alt="image" src="https://github.com/user-attachments/assets/606cd464-6f54-46ae-b8f2-63eb2de77ee1" />

<img width="616" height="430" alt="image" src="https://github.com/user-attachments/assets/18765fea-3dd2-4bf2-b67d-487def890447" />

<img width="577" height="582" alt="image" src="https://github.com/user-attachments/assets/9120a7dd-19b8-4131-9ca0-5ccc04bac08f" />

<img width="291" height="180" alt="image" src="https://github.com/user-attachments/assets/a865bfe2-e285-4d34-82a0-a67fa18a6435" />

<img width="513" height="276" alt="image" src="https://github.com/user-attachments/assets/87393a4c-11f4-4331-8724-3d9b89ba1726" />

<img width="560" height="268" alt="image" src="https://github.com/user-attachments/assets/34baf642-4aa5-413e-af77-5917e36f7acd" />

<img width="509" height="547" alt="image" src="https://github.com/user-attachments/assets/7eb5b0a4-e34c-44d4-bd79-4ff5fa126fd5" />








