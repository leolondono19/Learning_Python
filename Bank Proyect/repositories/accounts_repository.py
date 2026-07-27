import os
import json
from pathlib import Path
from typing import Any
from enums.account_type import TypeBankAccount
from enums.currency_type import TypeBankCurrency
from models.bank_account import BankAccount
from models.bank_customer import BankCustomer
from exceptions.exceptions import ValueNotFoundException

class AccountRepository:
    
    def __init__(self) -> None:
        BASE_DIR = Path(__file__).resolve().parent.parent
        self.file = BASE_DIR / "data" / "accounts.json"
    
    def save_account(self, accounts: list[BankAccount]):
        data: dict[str, Any] = { "accounts": [] }

        for account in accounts:
            data["accounts"].append(
                {
                    "account number": account.account_number,
                    "owner": account.owner.username,
                    "type account": account.type_account.value,
                    "type currency": account.type_currency.value,
                    "balance": account.balance
                }
            )

        with open(self.file, "w") as account_file:
            json.dump(data, account_file, indent=4)

    def load_accounts(self, customers: list[BankCustomer]) -> list[BankAccount]:
        accounts: list[BankAccount] = []
        if (not os.path.exists(self.file)):
            return []

        with open(self.file, "r") as account_file:
            data = json.load(account_file)

            for account_data in data["accounts"]:
                owner_username: str = account_data["owner"]

                owner: BankCustomer = self.find_customer_by_username(customers, owner_username)
                account: BankAccount = BankAccount(
                    owner,
                    TypeBankAccount(account_data["type account"]),
                    TypeBankCurrency(account_data["type currency"]),
                    account_data["balance"],
                    account_data["account number"]
                )
                accounts.append(account)

                owner.accounts.append(account)
        return accounts

    def find_customer_by_username(self, customers: list[BankCustomer], username: str) -> BankCustomer:
        for customer in customers:
            if customer.username == username:
                return customer
        raise ValueNotFoundException(username)
