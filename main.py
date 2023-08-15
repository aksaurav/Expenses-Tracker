# Main.py


def add_expense(date, description, amount):
    with open("expenses.txt", "a") as f:
        f.write(f"{date},{description},{amount}\n")
    print("Expense added successfully")


def view_expenses():
    with open("expenses.txt", "r") as f:
        expenses = f.readlines()
        for expense in expenses:
            date, description, amount = expense.strip().split(",")
            print(f"Date: {date} | Description: {description} | Amount: {amount}")


def main():
    while True:
        print("\nExpenses Tracker\n")
        print("1. Add Expenses")
        print("2. View Expense")
        print("3. Exit")

        choice = input("Select an Option: ")

        if choice == "1":
            date = input("Enter the Data (YYYY-MM-DD): ")
            description = input("Write a Description: ")
            amount = input("Enter the Amount: ")
            add_expense(date, description, amount)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("Exiting....")
            break

        else:
            print("Invalid choice. Try again")


if __name__ == "__main__":
    main()
