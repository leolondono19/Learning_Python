import random
from models.bank_customer import BankCustomer
from enums.account_type import TypeBankAccount
from enums.currency_type import TypeBankCurrency
from exceptions import exceptions

class BankAccount:
    used_account_numbers: set[str] = set()

    def __init__(
            self,
            owner: BankCustomer,
            type_account: TypeBankAccount,
            type_currency: TypeBankCurrency,
            balance: float = 0,
            account_number: str | None = None
            ) -> None:
        
        if account_number is None:
            self.account_number = self.__generate_account_number()
        else:
            self.account_number = account_number
            BankAccount.used_account_numbers.add(account_number)

        self.__balance = balance
        self.owner: BankCustomer = owner
        self.__type_account = type_account 
        self.__type_currency = type_currency 
    
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
        return f"{self.account_number} | {self.owner.username} | {self.__type_account.value} | {self.__balance} | {self.__type_currency.value}"
    
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
    
    def __generate_account_number(self) -> str:
        while True:
            self.account_number: str = str(random.randint(100000000, 999999999))

            if (self.account_number not in self.used_account_numbers):
                self.used_account_numbers.add(self.account_number)
                return self.account_number