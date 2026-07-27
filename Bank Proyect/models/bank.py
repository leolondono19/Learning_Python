from models.bank_account import BankAccount
from models.bank_customer import BankCustomer


class Bank:
    def __init__(
            self,
            name: str
            ) -> None:
        self.name = name
        self.customers: list[BankCustomer] = []