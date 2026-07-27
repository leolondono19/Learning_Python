import os
import json
from typing import Any
from pathlib import Path
from models.bank_customer import BankCustomer
from models.bank_account import BankAccount
from repositories.accounts_repository import AccountRepository

class CustomerRepository:
    def __init__(self) -> None:
        BASE_DIR = Path(__file__).resolve().parent.parent
        self.file = BASE_DIR / "data" / "customers.json"


    def save_customer(self, users: list[BankCustomer]):
        data: dict[str, Any] = { "users": [] }

        for user in users:
            data["users"].append(
                {
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "age": user.age,
                    "phone": user.phone,
                    "mail": user.mail,
                    "password": user.password,
                }
            )

        with open(self.file, "w") as account_file:
            json.dump(data, account_file, indent=4)

    def load_customers(self) -> list[BankCustomer]:
        customers: list[BankCustomer] = []

        if (not os.path.exists(self.file)):
            return []

        with open(self.file, "r") as account_file:
            data = json.load(account_file)

            for customer_data in data["users"]:
                customer: BankCustomer = BankCustomer(
                    customer_data["username"],
                    customer_data["password"],
                    customer_data["first_name"],
                    customer_data["last_name"],
                    customer_data["age"],
                    customer_data["phone"],
                    customer_data["mail"]
                )
                customers.append(customer)
                """
                for customer in customers:
                    for account in self.accounts:
                        if customer.username == account.owner.username:
                            customer.accounts.append()
                """
                
                #TODO: read accounts from the repository. Add the accounts for each user. 
        #foreach customer then customer.accouts.add()
        return customers