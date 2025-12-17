expenses = []

while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        expenses.append((amount, category))
        print("Expense added.")

    elif choice == "2":
        print("\nExpenses:")
        for exp in expenses:
            print(f"₹{exp[0]} - {exp[1]}")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
