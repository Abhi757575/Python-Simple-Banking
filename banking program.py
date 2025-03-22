#Python Banking Program

def show_balance(balance):
    print("-----------------Python Bank----------------------")
    print(f"Your Balance is ${balance:.3f}")
def deposit():
    print("-----------------Python Bank----------------------")
    amount = float(input("Enter the amount to be deposited:"))

    if amount < 0:
        print("-----------------Python Bank----------------------")
        print("Add a valid amount")
        return 0

    else:
        print("-----------------Python Bank----------------------")
        print(f"${amount} added successfully to your account")
        return amount
def withdraw(balance):
    print("-----------------Python Bank----------------------")
    amount = float(input("Enter the amount to be Withdrawn:"))

    if amount > balance:
        print("-----------------Python Bank----------------------")
        print("Insufficient Funds")
        return 0
    elif amount < 0:
        print("-----------------Python Bank----------------------")
        print("Add a valid amount")
        return 0
    else:
        return amount



def main():
    balance = 0
    is_running = True

    while is_running:
        print("-----------------Python Bank----------------------")
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter Your Choice(1-4): ")
        print("--------------------------------------------------")


        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("-----------------Python Bank----------------------")
            print("That is not a valid choice")
    print("-----------------Python Bank----------------------")
    print("Have a nice day")
    print("--------------------------------------------------")

if __name__ == '__main__':
    main()
