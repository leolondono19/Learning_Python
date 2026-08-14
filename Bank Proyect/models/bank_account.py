import random
from models.bank_customer import BankCustomer
from enums.account_type import TypeBankAccount
from enums.currency_type import TypeBankCurrency
from exceptions import exceptions

class BankAccount:
    used_account_ids: set[str] = set()

    def __init__(
            self,
            bank_customer: BankCustomer,
            type_account: TypeBankAccount,
            type_currency: TypeBankCurrency,
            balance: float = 0,
            bank_account_id: int | None = None
        ) -> None:

        if bank_account_id is None:
            self.bank_account_id = self.__generate_account_id()
        else:
            self.bank_account_id = str(bank_account_id)
            self.used_account_ids.add(self.bank_account_id)

        self.bank_customer: BankCustomer = bank_customer
        self.__type_account = type_account 
        self.__type_currency = type_currency
        self.__balance = balance
    
    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def type_account(self) -> TypeBankAccount:
        return self.__type_account
    
    @property
    def type_currency(self) -> TypeBankCurrency:
        return self.__type_currency

    def __str__(self) -> str:
        return f"{self.bank_account_id} | {self.bank_customer.bank.bank_id} | {self.__type_account.value} | {self.__balance} | {self.__type_currency.value}"
    
    def deposit(self, amount: float):
            if amount <= 0:
                raise exceptions.InvalidAmountException(amount)

            self.__balance += amount

    def withdraw(self, amount: float):
            if amount <= 0:
                raise exceptions.InvalidAmountException(amount)

            if amount > self.__balance:
                raise exceptions.InsufficientFundsException(self.__balance, amount)

            self.__balance -= amount
    
    def __generate_account_id(self) -> str:
        while True:
            self.bank_account_id: str = str(random.randint(1000, 1999))

            if (self.bank_account_id not in self.used_account_ids):
                self.used_account_ids.add(self.bank_account_id)
                return self.bank_account_id