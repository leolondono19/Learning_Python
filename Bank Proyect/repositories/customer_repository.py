import os
import json
from typing import Any
from pathlib import Path
from models.customer import Customer
from exceptions.exceptions import ValueNotFoundException

class CustomerRepository:
    def __init__(self) -> None:
        BASE_DIR = Path(__file__).resolve().parent.parent
        self.file = BASE_DIR / "data" / "customers.json"
        self.customers: list[Customer] = []
        self.load_customers()


    def save_customer(self):
        data: dict[str, Any] = { "customers": [] }

        for customer in self.customers:
            data["customers"].append(
                {
                    "customer id": customer.customer_id,
                    "username": customer.username,
                    "first_name": customer.first_name,
                    "last_name": customer.last_name,
                    "age": customer.age,
                    "phone": customer.phone,
                    "mail": customer.mail,
                    "password": customer.password
                }
            )

        with open(self.file, "w") as account_file:
            json.dump(data, account_file, indent=4)

    def load_customers(self) -> list[Customer]:
        if (not os.path.exists(self.file)):
            return []

        with open(self.file, "r") as account_file:
            data = json.load(account_file)

            for customer_data in data["customers"]:
                customer: Customer = Customer(
                    customer_data["username"],
                    customer_data["password"],
                    customer_data["first_name"],
                    customer_data["last_name"],
                    customer_data["age"],
                    customer_data["phone"],
                    customer_data["mail"],
                    customer_data["customer id"]
                )
                self.customers.append(customer)
                
        return self.customers

    def find_customer_by_id(self, customer_id: str) -> Customer:
            for customer in self.customers:
                if customer.customer_id == customer_id:
                    return customer
            raise ValueNotFoundException(customer_id)