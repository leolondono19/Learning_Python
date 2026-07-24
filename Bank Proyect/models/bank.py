from models.bank_account import BankAccount
from models.bank_customer import BankCustomer


class Bank:
    customers: list[BankCustomer]
    def __init__(
            self,
            name: str
            ) -> None:
        self.name = name