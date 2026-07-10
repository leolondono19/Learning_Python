from enum import Enum

import os
import json
from typing import Any










    









def show_accounts(bank_manager: BankManager) -> None:
    for account in bank_manager.accounts_list:
        print(
                f"{account.account_number} | "
                f"{account.owner} | "
                f"{account.type_account.value} | "
                f"{account.balance} | "
                f"{account.currency.value}"
            )



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
        #bank_manager.create_account(, type_account, type_currency)

    if (option == "3"):
        clear_display()
        while True:
            show_Atm_menu()
            option: str = input("What do you want to do?: ")
            if option == "1":
                amount: float = float(input("Please insert the amount you want to deposit:\n"))
                #AtmManager.deposit(amount)

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


        
        



