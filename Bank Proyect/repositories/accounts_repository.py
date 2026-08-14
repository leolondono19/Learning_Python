import os
import json
from pathlib import Path
from typing import Any
from enums.account_type import TypeBankAccount
from enums.currency_type import TypeBankCurrency
from models.bank_account import BankAccount
from models.bank_customer import BankCustomer
from repositories.bank_customer_repository import BankCustomerRepository

class AccountRepository:
    
    def __init__(self, bank_customer_repository: BankCustomerRepository) -> None:
        BASE_DIR = Path(__file__).resolve().parent.parent
        self.file = BASE_DIR / "data" / "accounts.json"
        self.accounts: list[BankAccount] = []
        self.bank_customer_repository: BankCustomerRepository = bank_customer_repository
        self.load_accounts()       
    
    def save_account(self):
        data: dict[str, Any] = { "accounts": [] }

        for account in self.accounts:
            data["accounts"].append(
                {
                    "bank account id": account.bank_account_id,
                    "bank customer id": account.bank_customer.bank_customer_id,
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
                bank_customer_id: str = account_data["bank customer id"]

                bank_customer: BankCustomer = self.bank_customer_repository.find_bank_customer_by_id(bank_customer_id)

                account: BankAccount = BankAccount(
                    bank_customer,
                    TypeBankAccount(account_data["type account"]),
                    TypeBankCurrency(account_data["type currency"]),
                    account_data["balance"],
                    account_data["bank account id"]
                )
                self.accounts.append(account)
                bank_customer.bank_accounts.append(account)

        return self.accounts
