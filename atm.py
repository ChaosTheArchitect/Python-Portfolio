from CardHolder import CardHolder

def print_menu():
    # Print options to the user
    print("Please choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

def deposit(user):
    try:
        deposit_amount = float(input("How much $$ would you like to Deposit: "))
        user.set_balance(user.get_balance() + deposit_amount)
        print("Thank you for your deposit. Your new balance is: ", str(user.get_balance()))
    except ValueError as e:
        print(f"Error: {e}")
        print("Invalid input")

def withdraw(user):
    try:
        withdraw_amount = float(input("How much $$ would you like to Withdraw: "))
        if user.get_balance() < withdraw_amount:
            print("Insufficient balance")
        else:
            user.set_balance(user.get_balance() - withdraw_amount)
            print("Your withdrawal was successful. Your new balance is: ", str(user.get_balance()))
    except ValueError as e:
        print(f"Error: {e}")
        print("Invalid Input")


def check_balance(user):
    print("Your current balance is: ", user.get_balance())

if __name__ == "__main__":
    current_user = CardHolder("", "", "", "", "0.0")  # Initial balance set to 0

    # Create a repo of CardHolders
    list_of_CardHolders = [
        CardHolder("4175964532552", 1234, "Enni", "Ruhl", "1000000.00"),
        CardHolder("5174918532150", 4321, "Marlin", "Bautista-Nunez", "1000000.00"),
        CardHolder("0173953532359", 1324, "Nilvia", "Bautista-Nunez", "1000000.00"),
        CardHolder("2179999532758", 2413, "Tieryn", "Ruhl", "-1000000.00")
    ]

    # Prompt user for debit card number
    while True:
        debit_cardnum = input("Please insert your debit card: ")
        # Check against repo
        debitMatch = [holder for holder in list_of_CardHolders if holder.get_cardnum() == debit_cardnum]
        if len(debitMatch) > 0:
            current_user = debitMatch[0]
            break
        else:
            print("Card number not recognized. Please try again.")

    # Prompt for PIN
    while True:
        try:
            userPin = int(input("Please enter your PIN: ").strip())
            if current_user.get_pin() == userPin:
                break
            else:
                print("Invalid PIN. Please try again.")
        except ValueError:
            print("Invalid PIN. Please try again.")

    # Print options
    print("Welcome ", current_user.get_firstname())
    option = 0
    while True:
        print_menu()
        try:
            option = int(input())
            if option == 1:
                deposit(current_user)
            elif option == 2:
                withdraw(current_user)
            elif option == 3:
                check_balance(current_user)
            elif option == 4:
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

    print("Thank you, Have a nice day.")
