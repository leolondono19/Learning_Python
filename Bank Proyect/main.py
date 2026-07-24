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






bank_manager: BankManager = BankManager("Bank_Accounts", "Users")

while True:
    clear_display()
    show_bank_menu()
    option: str = input("What do you want to do?: ")
    if (option == "1"):
        clear_display()
        print("-----------WELCOME TO YOUR BANK-----------")
        

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


        
        



