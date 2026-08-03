#from models.bank_account import BankAccount
from models.bank_customer import BankCustomer


class Bank:
    def __init__(
            self,
            name: str,
            bank_code: str
            ) -> None:
        self.__name = name
        self.__bank_code = bank_code
        self.customers: list[BankCustomer] = []

    @property
    def name(self) -> str:
        return self.__name

    @property
    def bank_code(self) -> str:
        return self.__bank_code