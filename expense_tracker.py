
from datetime import date

def add_expense(data):
    name = input("Enter expense name: ").strip()

    if not name:
        print("Expense name cannot be empty!")
        return

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero!")
            return
    except ValueError:
        print("Please enter a valid amount!")
        return

    category = input("Enter category: ").strip().title()

    if not category:
        category = "Uncategorized"

    date_string = input(
        "Enter date (YYYY-MM-DD) or press Enter for today: "
    ).strip()

    if not date_string:
        date_string = date.today().isoformat()
    else:
        try:
            year, month, day = map(int, date_string.split("-"))
            date(year, month, day)
            date_string = date(year, month, day).isoformat()
        except (ValueError, TypeError):
            print("Invalid date! Using today's date.")
            date_string = date.today().isoformat()

    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": date_string
    }

    data["expenses"].append(expense)
    print("Expense added successfully!")

    check_budget(data)


def view_expenses(data):
    if not data["expenses"]:
        print("No expenses recorded.")
        return

    print("\n===== EXPENSE LOG =====")

    for i, item in enumerate(data["expenses"], start=1):
        print(f"{i}. Date: {item['date']}")
        print(f"   Name: {item['name']}")
        print(f"   Amount: Rs. {item['amount']:.2f}")
        print(f"   Category: {item['category']}")


def show_total(data):
    total = sum(item["amount"] for item in data["expenses"])

    print("\nTotal Expenditure: Rs.", round(total, 2))


def category_summary(data):
    if not data["expenses"]:
        print("No expenses recorded.")
        return

    summary = {}

    for item in data["expenses"]:
        category = item["category"]
        summary[category] = (
            summary.get(category, 0) + item["amount"]
        )

    print("\n===== CATEGORY SUMMARY =====")

    for category, amount in summary.items():
        print(f"{category}: Rs. {amount:.2f}")


def set_budget(data):
    try:
        budget = float(input("Enter monthly budget (Rs.): "))

        if budget < 0:
            print("Budget cannot be negative!")
            return

        data["budget"] = budget
        print(f"Monthly budget set to Rs. {budget:.2f}")

        check_budget(data)

    except ValueError:
        print("Please enter a valid budget amount!")


def check_budget(data):
    budget = data["budget"]

    if budget <= 0:
        return

    current_month = date.today().strftime("%Y-%m")

    monthly_total = sum(
        item["amount"]
        for item in data["expenses"]
        if item["date"].startswith(current_month)
    )

    print("\n===== BUDGET TRACKER =====")
    print(f"Monthly spending: Rs. {monthly_total:.2f}")
    print(f"Monthly budget: Rs. {budget:.2f}")
    print(f"Remaining budget: Rs. {budget - monthly_total:.2f}")

    if monthly_total > budget:
        print("WARNING! You have exceeded your budget!")


def monthly_report(data):
    if not data["expenses"]:
        print("No expenses available for the report.")
        return

    months = {}

    for item in data["expenses"]:
        month = item["date"][:7]

        if month not in months:
            months[month] = []

        months[month].append(item)

    print("\n===== MONTHLY EXPENSE REPORT =====")

    for month in sorted(months, reverse=True):
        records = months[month]
        total = sum(item["amount"] for item in records)

        print(f"\nMonth: {month}")
        print(f"Total: Rs. {total:.2f}")

        for item in records:
            print(
                f"- {item['date']} | {item['name']} | "
                f"Rs. {item['amount']:.2f} | {item['category']}"
            )


def main():
    data = {
        "expenses": [],
        "budget": 0.0
    }

    while True:
        print("\n===== EXPENSE MANAGEMENT SYSTEM =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expenditure")
        print("4. Category Summary")
        print("5. Set Monthly Budget")
        print("6. Monthly Expense Report")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_expense(data)

        elif choice == "2":
            view_expenses(data)

        elif choice == "3":
            show_total(data)

        elif choice == "4":
            category_summary(data)

        elif choice == "5":
            set_budget(data)

        elif choice == "6":
            monthly_report(data)

        elif choice == "7":
            print("Thank you for using Expense Management System!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
