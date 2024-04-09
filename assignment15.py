class bankacc:
    def __init__(self, name, balance, address, age, phone_number):
        self.name = name
        self.balance = balance
        self.address = address
        self.age = age
        self.phone_number = phone_number

    def depositammount(self, amount):
            self.balance += amount
            print(f"Amount {amount} deposited successfully.")

    def withdrawammount(self, amount):
        if self.balance - amount >= 2000:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully.")
        else:
            print("Insufficient balance. Minimum balance of 2000 must be maintained.")

    def showbalance(self):
        print(f"Current balance: {self.balance}")

    def showinfo(self):
        print(f"Account Holder: {self.name}\nBalance: {self.balance}\nAddress: {self.address}\nAge: {self.age}\nPhone Number: {self.phone_number}")

def main():
    name = input("Enter account holder's name: ")
    age = int(input("Enter account holder's age: "))
    address = input("Enter account holder's address: ")
    phone_number = input("Enter account holder's phone number: ")
    initial_balance = 0  

    account = bankacc(name, initial_balance, address, age, phone_number)

    while (choice != 0):
        print("\n1. Deposit Amount\n2. Withdraw Amount\n3. Display Balance\n4. Display Statement\n5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 3:
            account.display_balance()
        elif choice == 4:
            account.display_statement()
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

