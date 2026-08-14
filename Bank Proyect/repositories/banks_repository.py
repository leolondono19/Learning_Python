import os
import json
from typing import Any
from pathlib import Path
from models.bank import Bank
from exceptions.exceptions import ValueNotFoundException

class BankRepository:
    def __init__(self) -> None:
        BASE_DIR = Path(__file__).resolve().parent.parent
        self.file = BASE_DIR / "data" / "banks.json"
        self.banks: list[Bank] = []
        self.load_banks()
    
    def save_bank(self):
        data: dict[str, Any] = { "banks": [] }

        for bank in self.banks:
            data["banks"].append(
                {
                    "bank id": bank.bank_id,
                    "name": bank.name,
                    "bank code": bank.bank_code
                }
            )

        with open(self.file, "w") as account_file:
            json.dump(data, account_file, indent=4)

    def load_banks(self) -> list[Bank]:
        if (not os.path.exists(self.file)):
            return []

        with open(self.file, "r") as account_file:
            data = json.load(account_file)

            for account_data in data["accounts"]:
                account: Bank = Bank(
                    account_data["name"],
                    account_data["bank code"],
                    account_data["bank id"]
                )
                self.banks.append(account)

        return self.banks

    def find_bank_by_id(self, bank_id: str) -> Bank:
        for bank in self.banks:
            if bank.bank_id == bank_id:
                return bank
        raise ValueNotFoundException(bank_id)
