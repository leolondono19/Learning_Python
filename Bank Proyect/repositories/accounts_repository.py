import os
import json
from pathlib import Path
from typing import Any
from enums.account_type import TypeBankAccount
from enums.currency_type import TypeBankCurrency
from models.bank_account import BankAccount
from models.bank_customer import BankCustomer
from repositories.customer_repository import CustomerRepository

class AccountRepository:
    
    def __init__(self, customer_repository: CustomerRepository) -> None:
        BASE_DIR = Path(__file__).resolve().parent.parent
        self.file = BASE_DIR / "data" / "accounts.json"
        self.accounts: list[BankAccount] = []
        self.customer_repository: CustomerRepository = customer_repository
        self.customers: list[BankCustomer] = customer_repository.customers
        self.load_accounts()
        

    
    def save_account(self):
        data: dict[str, Any] = { "accounts": [] }

        for account in self.accounts:
            data["accounts"].append(
                {
                    "account id": account.account_id,
                    "owner": account.owner.username,
                    "type account": account.type_account.value,
                    "type currency": account.type_currency.value,
                    "balance": account.balance
                }
            )

        with open(self.file, "w") as account_file:
            json.dump(data, account_file, indent=4)

    def load_accounts(self) -> list[BankAccount]:
        if (not os.path.exists(self.file)):
            return []

        with open(self.file, "r") as account_file:
            data = json.load(account_file)

            for account_data in data["accounts"]:
                owner_username: str = account_data["owner"]

                owner: BankCustomer = self.customer_repository.find_customer_by_username(owner_username)
                account: BankAccount = BankAccount(
                    owner,
                    TypeBankAccount(account_data["type account"]),
                    TypeBankCurrency(account_data["type currency"]),
                    account_data["balance"],
                    account_data["account id"]
                )
                #self.accounts.clear()
                self.accounts.append(account)

                owner.accounts.append(account)
        return self.accounts
