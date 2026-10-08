expenses = []

while True:
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append((item, amount))
        print("Expense added!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses yet.")
        else:
            print("\nYour Expenses:")
            for i, (item, amount) in enumerate(expenses, 1):
                print(i, ".", item, "-", amount)

    elif choice == "3":
        total = sum(amount for item, amount in expenses)
        print("Total Expenses:", total)

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")
