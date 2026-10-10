import json
import os
from datetime import datetime

# Global configuration constants
DATA_FILE = "expenses_data.json"

def load_data():
    """Reads system state from the local data file."""
    if not os.path.exists(DATA_FILE):
        return {"expenses": [], "budget": 0.0}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Notice: Error reading data file. Initializing fresh workspace.")
        return {"expenses": [], "budget": 0.0}

def save_data(data):
    """Writes current system state to the local data file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except IOError:
        print("Error: Persistent data save failed.")

def add_expense(data):
    """Processes input loops to safely add new expense maps."""
    name = input("Enter expense name: ").strip()
    if not name:
        print("Error: Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Error: Amount must be greater than zero.")
            return
    except ValueError:
        print("Error: Invalid input. Amount must be a valid number.")
        return

    category = input("Enter category: ").strip().title()
    if not category:
        category = "Uncategorized"

    date_string = input("Enter date (YYYY-MM-DD) or press Enter for current date: ").strip()
    if not date_string:
        date_string = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date_string, "%Y-%m-%d")
        except ValueError:
            print("Error: Invalid date format. Defaulting to current date.")
            date_string = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": date_string
    }

    data["expenses"].append(expense)
    save_data(data)
    print("Success: Expense registered securely.")

    # Evaluate budget overhead metrics immediately
    check_budget(data)

def view_expenses(data):
    """Outputs all recorded transactions chronologically."""
    if not data["expenses"]:
        print("No expense records discovered.")
        return

    print("\n--- Expense Log ---")
    for index, item in enumerate(data["expenses"], start=1):
        print(f"{index}. Date: {item['date']} | Name: {item['name']} | Amount: {item['amount']:.2f} | Category: {item['category']}")

def show_total(data):
    """Calculates cumulative sum of all financial transactions."""
    total = sum(item["amount"] for item in data["expenses"])
    print(f"Total Combined Expenditures: {total:.2f}")
    return total

def category_summary(data):
    """Groups financial entries into distinct logical domains."""
    if not data["expenses"]:
        print("No expense records discovered.")
        return

    summary = {}
    for item in data["expenses"]:
        cat = item["category"]
        summary[cat] = summary.get(cat, 0.0) + item["amount"]

    print("\n--- Structural Domain Summary ---")
    for cat, total in summary.items():
        print(f"Domain: {cat} | Combined Outflow: {total:.2f}")

def set_budget(data):
    """Modifies structural limitation values for target tracking."""
    try:
        new_limit = float(input("Enter maximum monthly budget threshold: "))
        if new_limit < 0:
            print("Error: Budget limitations cannot be negative integers.")
            return
        data["budget"] = new_limit
        save_data(data)
        print(f"Success: Monthly limitation boundary targeted at {data['budget']:.2f}")
    except ValueError:
        print("Error: Budget parameters must be numeric values.")

def check_budget(data):
    """Measures variance parameters between active entries and limitations."""
    if data["budget"] <= 0:
        return

    current_month = datetime.now().strftime("%Y-%m")
    monthly_outflow = sum(
        item["amount"] for item in data["expenses"] if item["date"].startswith(current_month)
    )

    print(f"Budget Tracking Notification: Current Month Usage stands at {monthly_outflow:.2f} / {data['budget']:.2f}")
    if monthly_outflow > data["budget"]:
        overage = monthly_outflow - data["budget"]
        print(f"Warning Alert: Consumption parameters exceed limitations by {overage:.2f}")

def generate_monthly_report(data):
    """Splits tracking histories down into distinct dynamic monthly buckets."""
    if not data["expenses"]:
        print("No operational entries available to parse data frameworks.")
        return

    monthly_buckets = {}
    for item in data["expenses"]:
        # Extract the YYYY-MM component out of the YYYY-MM-DD sequence
        month_key = item["date"][:7]
        if month_key not in monthly_buckets:
            monthly_buckets[month_key] = []
        monthly_buckets[month_key].append(item)

    print("\n--- Categorized Monthly Reports ---")
    for month, records in sorted(monthly_buckets.items(), reverse=True):
        month_sum = sum(rec["amount"] for rec in records)
        print(f"\nPeriod Framework: {month}")
        print(f"Total Outflow Profile: {month_sum:.2f}")
        print("Associated Period Entries:")
        for rec in records:
            print(f"  - [{rec['date']}] {rec['name']}: {rec['amount']:.2f} ({rec['category']})")

def main():
    """Initializes main interface looping sequence."""
    runtime_data = load_data()

    while True:
        print("\n===== EXPENSE MANAGEMENT INTERFACE V4 =====")
        print("1. Add Expense")
        print("2. View Expenses Log")
        print("3. Show Total Expenditures")
        print("4. Category Domain Breakdown")
        print("5. Configure Spending Budget Ceiling")
        print("6. Extract Chronological Monthly Reports")
        print("7. Exit Application Engine")

        choice = input("Enter choice parameter (1-7): ").strip()

        if choice == "1":
            add_expense(runtime_data)
        elif choice == "2":
            view_expenses(runtime_data)
        elif choice == "3":
            show_total(runtime_data)
        elif choice == "4":
            category_summary(runtime_data)
        elif choice == "5":
            set_budget(runtime_data)
        elif choice == "6":
            generate_monthly_report(runtime_data)
        elif choice == "7":
            print("System down cycle confirmed. Terminating engine loops.")
            break
        else:
            print("Error: Input criteria does not match defined menu nodes. Retry sequence.")

if __name__ == "__main__":
    main()
