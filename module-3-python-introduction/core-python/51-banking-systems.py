# BANKING MANAGEMENT SYSTEM
accounts = {}
while True:
    print("\n===== BANKING MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # CREATE ACCOUNT
    if choice == '1':
        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:
            print("Account already exists!")
        else:
            name = input("Enter Account Holder Name: ")
            balance = float(input("Enter Initial Balance: "))

            accounts[acc_no] = {
                "name": name,
                "balance": balance
            }

            print("Account Created Successfully!")

    # VIEW ACCOUNTS
    elif choice == '2':
        if not accounts:
            print("No accounts found.")
        else:
            print("\n--- ACCOUNT DETAILS ---")
            for acc_no, details in accounts.items():
                print(f"Account No: {acc_no}")
                print(f"Name      : {details['name']}")
                print(f"Balance   : ₹{details['balance']}")
                print("--------------------------")

    # DEPOSIT MONEY
    elif choice == '3':
        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:
            amount = float(input("Enter Deposit Amount: "))

            accounts[acc_no]["balance"] += amount

            print("Amount Deposited Successfully!")
            print(f"New Balance: ₹{accounts[acc_no]['balance']}")
        else:
            print("Account not found!")

    # WITHDRAW MONEY
    elif choice == '4':
        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:
            amount = float(input("Enter Withdrawal Amount: "))

            if amount <= accounts[acc_no]["balance"]:
                accounts[acc_no]["balance"] -= amount

                print("Withdrawal Successful!")
                print(f"Remaining Balance: ₹{accounts[acc_no]['balance']}")
            else:
                print("Insufficient Balance!")
        else:
            print("Account not found!")

    # EXIT
    elif choice == '5':
        print("Thank you for using Banking Management System.")
        break

    else:
        print("Invalid choice! Please try again.")