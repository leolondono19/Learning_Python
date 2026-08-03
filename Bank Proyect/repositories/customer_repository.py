import os
import json
from typing import Any
from pathlib import Path
from models.bank_customer import BankCustomer
from exceptions.exceptions import ValueNotFoundException

class CustomerRepository:
    def __init__(self) -> None:
        BASE_DIR = Path(__file__).resolve().parent.parent
        self.file = BASE_DIR / "data" / "customers.json"
        self.customers: list[BankCustomer] = []
        self.load_customers()


    def save_customer(self):
        data: dict[str, Any] = { "users": [] }

        for user in self.customers:
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
                #self.customers.clear()
                self.customers.append(customer)
                
        return self.customers

    def find_customer_by_username(self, username: str) -> BankCustomer:
            for customer in self.customers:
                if customer.username == username:
                    return customer
            raise ValueNotFoundException(username)