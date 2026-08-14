import os
import json
from pathlib import Path
from typing import Any
from models.bank import Bank
from models.customer import Customer
from models.bank_customer import BankCustomer
from repositories.banks_repository import BankRepository
from repositories.customer_repository import CustomerRepository
from exceptions.exceptions import ValueNotFoundException

class BankCustomerRepository:
    
    def __init__(self, customer_repository: CustomerRepository, bank_repository: BankRepository) -> None:
        BASE_DIR = Path(__file__).resolve().parent.parent
        self.file = BASE_DIR / "data" / "accounts.json"
        self.bank_customers: list[BankCustomer] = []
        self.bank_repository: BankRepository = bank_repository
        self.customer_repository: CustomerRepository = customer_repository
        self.load_bank_customers()       
    
    def save_bank_customer(self):
        data: dict[str, Any] = { "bank customers": [] }

        for bank_customer in self.bank_customers:
            data["bank customers"].append(
                {
                    "bank customer id": bank_customer.bank_customer_id,
                    "customer id": bank_customer.customer.customer_id,
                    "bank id": bank_customer.bank.bank_id
                }
            )

        with open(self.file, "w") as account_file:
            json.dump(data, account_file, indent=4)

    def load_bank_customers(self) -> list[BankCustomer]:
        if (not os.path.exists(self.file)):
            return []

        with open(self.file, "r") as account_file:
            data = json.load(account_file)

            for account_data in data["accounts"]:
                customer_id: str = account_data["customer id"]
                bank_id: str = account_data["bank id"]

                customer: Customer = self.customer_repository.find_customer_by_id(customer_id)
                bank: Bank = self.bank_repository.find_bank_by_id(bank_id)
                bank_customer: BankCustomer = BankCustomer(
                    customer,
                    bank,
                    account_data["bank customer id"]
                )
                self.bank_customers.append(bank_customer)
        return self.bank_customers

    def find_bank_customer_by_id(self, bank_customer_id: str) -> BankCustomer:
        for bank_customer in self.bank_customers:
            if bank_customer.bank_customer_id == bank_customer_id:
                return bank_customer
        raise ValueNotFoundException(bank_customer_id)
