import os
import json
from pathlib import Path
from typing import Any
from models.bank_account import BankAccount

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

    def load_accounts(self) -> list[BankAccount]:
        accounts: list[BankAccount] = []
        if (not os.path.exists(self.file)):
            return []

        with open(self.file, "r") as account_file:
            data = json.load(account_file)

            for account_data in data["accounts"]:
                account: BankAccount = BankAccount(
                    account_data["owner"],
                    account_data["type account"],
                    account_data["type currency"]
                )
                account_data["account number"]
                account_data["balance"]

                accounts.append(account)
        return accounts
