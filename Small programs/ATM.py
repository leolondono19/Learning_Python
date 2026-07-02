import os
import json
from typing import Any


class BankAccount:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance


class ATM:
    def __init__(self, file: str) -> None:
        self.file = file
        self.accounts: list[BankAccount] = []
        self.load()

    def create_account(self):
        owner: str = input("Insert account owner:\n")

        if self.find_account(owner):
            print("Account already exists")
            return

        account: BankAccount = BankAccount(owner, 0)
        self.accounts.append(account)

        print("Account successfully created")

    def find_account(self, owner: str) -> BankAccount | None:
        for account in self.accounts:
            if account.owner.lower() == owner.lower():
                return account

        return None

    def show_accounts(self):
        if len(self.accounts) == 0:
            print("No accounts found")
            return
        print("----- Accounts -----")

        for index, account in enumerate(self.accounts, start=1):
            print(
                f"{index}. "
                f"{account.owner} | "
                f"${account.balance:.2f}"
            )

    def deposit(self):

        owner: str = input("Account owner:\n")

        account: BankAccount | None = self.find_account(owner)

        if account is None:
            print("Account not found")
            return

        try:
            amount: float = float(input("Insert amount to deposit:\n"))

            if amount <= 0:
                print("Invalid amount")
                return

            account.balance += amount

            print(
                f"Deposit successful.\n"
                f"New balance: "
                f"${account.balance:.2f}"
            )

        except ValueError:
            print("Invalid amount")

    def withdraw(self):

        owner: str = input("Account owner:\n")

        account: BankAccount | None = self.find_account(owner)

        if account is None:
            print("Account not found")
            return

        try:
            amount: float = float(input("Insert amount to withdraw:\n"))

            if amount <= 0:
                print("Invalid amount")
                return

            if amount > account.balance:
                print("Insufficient funds")
                return

            account.balance -= amount

            print(
                f"Withdraw successful.\n"
                f"New balance: "
                f"${account.balance:.2f}"
            )

        except ValueError:
            print("Invalid amount")

    def save(self):

        data: dict[str, Any] = { "accounts": [] }

        for account in self.accounts:
            data["accounts"].append(
                {
                    "owner": account.owner,
                    "balance": account.balance
                }
            )

        with open(self.file, "w") as account_file:
            json.dump(data, account_file, indent=4)

    def load(self):

        if not os.path.exists(self.file):
            return

        with open(self.file, "r") as account_file:

            data = json.load(account_file)

            for account_data in data["accounts"]:

                account: BankAccount = BankAccount(
                    account_data["owner"],
                    account_data["balance"]
                )

                self.accounts.append(account)


def show_menu() -> None:
    print("\n===== ATM SYSTEM =====")
    print("1. Create Account")
    print("2. Show Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")


def clear_display() -> None:
    os.system("cls")


def pause_display() -> None:
    os.system("pause")


atm: ATM = ATM("accounts.json")

while True:

    clear_display()
    show_menu()

    option: str = input("Select an option:\n")

    if option == "1":
        clear_display()
        atm.create_account()
        atm.save()
        pause_display()

    elif option == "2":
        clear_display()
        atm.show_accounts()
        pause_display()

    elif option == "3":
        clear_display()
        atm.deposit()
        atm.save()
        pause_display()

    elif option == "4":
        clear_display()
        atm.withdraw()
        atm.save()
        pause_display()

    elif option == "5":
        atm.save()
        clear_display()
        print("Thanks for using the ATM")
        break

    else:
        print("Invalid option")
        pause_display()