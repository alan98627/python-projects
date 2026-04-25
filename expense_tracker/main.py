import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    name = input("Enter expense name: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    expenses.append({"name": name, "amount": amount})
    save_expenses(expenses)
    print("Expense added.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    for i, exp in enumerate(expenses):
        print(f"{i + 1}. {exp['name']} - ${exp['amount']}")


def show_total(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total expenses: ${total}")


def main():
    expenses = load_expenses()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()