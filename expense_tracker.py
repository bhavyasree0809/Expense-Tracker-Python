
# Expense Tracker - Version 3

expenses = []

def add_expense():
    name = input("Enter expense name: ")

    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        category = input("Enter category: ")

        expense = {
            "name": name,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)
        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount! Enter a number.")

def view_expenses():
    if not expenses:
        print("No expenses found!")
        return

    print("\n--- Expense History ---")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - "
              f"₹{expense['amount']:.2f} "
              f"({expense['category']})")

def show_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total Expenses: ₹{total:.2f}")

def category_summary():
    if not expenses:
        print("No expenses found!")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"].title()
        summary[category] = (
            summary.get(category, 0) + expense["amount"]
        )

    print("\n--- Category Summary ---")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")

def main():
    while True:
        print("\n===== EXPENSE TRACKER V3 =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
            
