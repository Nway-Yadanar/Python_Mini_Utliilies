import os

def addexpense():
    expense = input("Description of the expense: ")
    amount = input("Amount: ")
    with open('expenses.txt' , 'a') as file:
        file.write(f"{expense}: ${amount}\n")
    print("Expense Successfully saved.")


def main():
    while True:
        print("\n💰 Expense Tracker Menu 💰")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()