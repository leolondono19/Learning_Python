import os
import json
from typing import Any
from models.bank import Bank

class BankRepository:
    def __init__(self) -> None:
        self.file = "data/banks.json"
    
    def save_account(self, banks: list[Bank]):
        data: dict[str, Any] = { "accounts": [] }

        for bank in banks:
            data["accounts"].append(
                {
                    "name": bank.name
                }
            )

        with open(self.file, "w") as account_file:
            json.dump(data, account_file, indent=4)

    def load_banks(self) -> list[Bank]:
        banks: list[Bank] = []
        if (not os.path.exists(self.file)):
            return []

        with open(self.file, "r") as account_file:
            data = json.load(account_file)

            for account_data in data["accounts"]:
                account: Bank = Bank(
                    account_data["name"],
                )
                banks.append(account)

                #TODO: Read user accounts. Add users to each bank. 
        return banks
