from models.bank_account import BankAccount
from models.customer import Customer
from models.bank import Bank
import random

class BankCustomer:
    used_bank_customer_ids: set[str] = set()

    def __init__(
            self,
            customer: Customer,
            bank: Bank,
            bank_customer_id: int | None = None
        ) -> None:
        
        if bank_customer_id is None:
            self.bank_customer_id = self.__generate_bank_customer_id()
        else:
            self.bank_customer_id = str(bank_customer_id)
            self.used_bank_customer_ids.add(self.bank_customer_id)
        self.customer = customer
        self.bank = bank
        self.bank_accounts: list[BankAccount] = []

    def __generate_bank_customer_id(self) -> str:
        while True:
            self.customer_id: str = str(random.randint(1000, 1999))

            if (self.customer_id not in self.used_bank_customer_ids):
                self.used_bank_customer_ids.add(self.customer_id)
                return f"{self.customer_id}" 


        