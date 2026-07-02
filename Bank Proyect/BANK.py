from enum import Enum
import random
import os
import json
from typing import Any

class TypeBankAccount(Enum):
    SAVING_ACCOUNT = "Saving Account"
    CHECKING_ACCOUNT = "Checking Account"

class TypeBankCurrency(Enum):
    DOLARS = "USD"
    BOLIVIANOS = "Bs"
    EUROS = "EUR"

class Role(Enum):
    ADMIN = "Administrator"
    CUSTOMER = "Customer"

class User:
    def __init__(
            self,
            username: str,
            name: str,
            surname: str,
            age: int,
            phone: int,
            mail: str
            ) -> None:
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.mail = mail
        self.role = Role.CUSTOMER

class BankAccount:
    used_account_numbers: set[str] = set()

    def __init__(
            self,
            owner: User,
            ) -> None:
        self.account_number = self._generate_account_number()
        self.owner: User = owner
        self.balance: float = 0
        self.type_account: TypeBankAccount = TypeBankAccount.SAVING_ACCOUNT
        self.currency: TypeBankCurrency = TypeBankCurrency.DOLARS
    
    def _generate_account_number(self) -> str:
        while True:
            self.account_number: str = str(random.randint(100000000, 999999999))

            if (self.account_number not in self.used_account_numbers):
                self.used_account_numbers.add(self.account_number)
                return self.account_number
    
class AtmManager:
    def __init__(self, bank_account: BankAccount) -> None:
        self.bank_account = bank_account

    def deposit(self, amount: float):
        try:
            if amount <= 0:
                print("Invalid amount")
                return

            self.bank_account.balance += amount

            print(
                f"Deposit successful.\n"
                f"New balance: "
                f"${self.bank_account.balance:.2f}"
            )

        except ValueError:
            print("Invalid amount")

    def withdraw(self, amount: float):
        try:
            if amount <= 0:
                print("Invalid amount")
                return

            if amount > self.bank_account.balance:
                print("Insufficient funds")
                return

            self.bank_account.balance -= amount

            print(
                f"Withdraw successful.\n"
                f"New balance: "
                f"${self.bank_account.balance:.2f}"
            )

        except ValueError:
            print("Invalid amount")



class Bank:
    def __init__(
            self,
            name: str,
            accounts: list[BankAccount],
            customers: list[User]
            ) -> None:
        pass

class BankManager:
    def __init__(self, accounts_file: str, users_file: str) -> None:
        self.accounts_file = accounts_file
        self.users_file = users_file
        self.load_accounts()
        self.load_users()

    accounts_list: list[BankAccount] = []
    users_list: list[User] = []
    user_accounts: list[BankAccount] = []

    def log_in(self, username: str) -> BankAccount:
        for account in self.accounts_list:
            if username == account.owner.username:
                return account

        raise ValueError("Account not found.")
    
    def log_in1(self, username: str) -> User:
        for user in self.users_list:
            if username == user.username:
                return user

        raise ValueError("User not found.")

    def create_user(self, username: str, name: str, surname: str, age: int, phone: int, mail: str, is_admin: str) -> None:
        user: User = User(username, name, surname, age, phone, mail)
        if is_admin == "y":
            admin_code: int = int(input("Enter the secret code:\n"))
            if admin_code == 1234:
                user.role = Role.ADMIN
            else: 
                return
        else:
            print("User successfully created!")
        
        self.users_list.append(user)
    
    def save_user(self):
        data: dict[str, Any] = { "users": [] }

        for user in self.users_list:
            data["users"].append(
                {
                    "username": user.username,
                    "name": user.name,
                    "surname": user.surname,
                    "age": user.age,
                    "phone": user.phone,
                    "mail": user.mail,
                    "role": user.role.value,
                }
            )

        with open(self.users_file, "w") as account_file:
            json.dump(data, account_file, indent=4)

    def load_users(self):
        if (not os.path.exists(self.users_file)):
            return

        with open(self.users_file, "r") as account_file:
            data = json.load(account_file)

            for user_data in data["users"]:
                user: User = User(
                    user_data["username"],
                    user_data["name"],
                    user_data["surname"],
                    user_data["age"],
                    user_data["phone"],
                    user_data["mail"],
                )

                self.users_list.append(user)

    def create_account(self, owner: User, choose_type_account: str, choose_currency: str) -> None:

        account: BankAccount = BankAccount(owner)

        if choose_type_account == "1":
            account.type_account = TypeBankAccount.SAVING_ACCOUNT
        elif choose_type_account == "2":
            account.type_account = TypeBankAccount.CHECKING_ACCOUNT

        if choose_currency == "1":
            account.currency = TypeBankCurrency.DOLARS
        elif choose_currency == "2":
            account.currency = TypeBankCurrency.BOLIVIANOS
        elif choose_currency == "3":
            account.currency = TypeBankCurrency.EUROS
        
        self.accounts_list.append(account)

    def save_account(self):
        data: dict[str, Any] = { "accounts": [] }

        for account in self.accounts_list:
            data["accounts"].append(
                {
                    "account number": account.account_number,
                    "owner": account.owner,
                    "type": account.type_account.value,
                    "balance": account.balance,
                    "currency": account.currency.value
                }
            )

        with open(self.accounts_file, "w") as account_file:
            json.dump(data, account_file, indent=4)

    def load_accounts(self):
        if (not os.path.exists(self.accounts_file)):
            return

        with open(self.accounts_file, "r") as account_file:
            data = json.load(account_file)

            for account_data in data["accounts"]:
                account: BankAccount = BankAccount(
                    account_data["owner"]
                )
                account.balance = account_data(["balance"])
                account.type_account = TypeBankAccount(account_data["type"])
                account.currency = TypeBankCurrency(account_data["currency"])

                self.accounts_list.append(account)
    
    def load_user_accounts(self):


def show_accounts(bank_manager: BankManager) -> None:
    for accounts in bank_manager.accounts_list:
        print(
                f"{accounts.account_number} | "
                f"{accounts.owner} | "
                f"{accounts.type_account.value} | "
                f"{accounts.balance} | "
                f"{accounts.currency.value}"
            )

def show_Atm_menu() -> None:
    print("\n----Welcome to your ATM operations----") 
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("5. Exit")

def show_bank_menu() -> None:
    print("\n----Welcome to your BANK----")
    print("1. Create User")
    print("2. Create Account")
    print("3. ATM")
    print("4. Delete a task")
    print("5. Show accounts")
    print("6. Exit")

def show_type_account_menu() -> None:
    print(f"1.- {TypeBankAccount.SAVING_ACCOUNT.value}")
    print(f"1.- {TypeBankAccount.CHECKING_ACCOUNT.value}")

def show_currency() -> None:
    print(f"1.- {TypeBankCurrency.DOLARS.value}")
    print(f"1.- {TypeBankCurrency.BOLIVIANOS.value}")
    print(f"1.- {TypeBankCurrency.EUROS.value}")

def clear_display() -> None:
    os.system("cls")

def pause_display() -> None:
    os.system("pause")


bank_manager: BankManager = BankManager("Bank_Accounts", "Users")

while True:
    clear_display()
    show_bank_menu()
    option: str = input("What do you want to do?: ")
    if (option == "1"):
        clear_display()
        print("-----------WELCOME TO YOUR BANK-----------")
        print("Complete your register:\n")
        username: str = input("Please insert your username (This will use for your bank account)\n")
        name: str = input("Please insert your name\n")
        surname: str = input("Please insert your surname\n")
        age: int = int(input("Please insert your age\n"))
        phone: int = int(input("Please insert your phone\n"))
        mail: str = input("Please insert your mail\n")
        is_admin: str = input("Is this an admin account? (y/n)")

        bank_manager.create_user(username, name, surname, age, phone, mail, is_admin)


    if (option == "2"):
        name: str = input("Please Insert your name\n")
        clear_display()
        show_type_account_menu()
        type_account: str = input("Please select your type account\n")
        clear_display()
        show_currency()
        type_currency: str = input("Please insert your type currency\n")
        clear_display()
        print("Your account was successfully created!!")
        pause_display()
        bank_manager.create_account(, type_account, type_currency)

    if (option == "3"):
        clear_display()
        while True:
            show_Atm_menu()
            option: str = input("What do you want to do?: ")
            if option == "1":
                amount: float = float(input("Please insert the amount you want to deposit:\n"))
                AtmManager.deposit(amount)

    if (option == "4"):
        pass

    if (option == "5"):
        clear_display()
        print("----------------------ACCOUNTS----------------------")
        show_accounts(bank_manager)
        pause_display()

    if (option == "6"):
        bank_manager.save_user()
        bank_manager.save_account()
        clear_display()
        print("Thanks for use this program")
        break


        
        



