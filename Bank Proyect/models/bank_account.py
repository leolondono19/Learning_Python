import random
from models.user import User
from enums.account_type import TypeBankAccount
from enums.currency_type import TypeBankCurrency

class BankAccount:
    used_account_numbers: set[str] = set()

    def __init__(
            self,
            owner: User,
            ) -> None:
        self.account_number = self._generate_account_number()
        self.owner: User = owner
        self.balance: float = 0
        self.type_account: TypeBankAccount = TypeBankAccount.SAVING_ACCOUNT
        self.currency: TypeBankCurrency = TypeBankCurrency.DOLARS
    
    def __str__(self) -> str:
        return f"{self.account_number} | {self.owner} | {self.type_account} | {self.balance} | {self.currency}"
    
    def deposit(self, amount: float):
        try:
            if amount <= 0:
                print("Invalid amount")
                return

            self.balance += amount

            print(
                f"Deposit successful.\n"
                f"New balance: "
                f"${self.balance:.2f}"
            )

        except ValueError:
            print("Invalid amount")

    def withdraw(self, amount: float):
        try:
            if amount <= 0:
                print("Invalid amount")
                return

            if amount > self.balance:
                print("Insufficient funds")
                return

            self.balance -= amount

            print(
                f"Withdraw successful.\n"
                f"New balance: "
                f"${self.balance:.2f}"
            )

        except ValueError:
            print("Invalid amount")
    
    def _generate_account_number(self) -> str:
        while True:
            self.account_number: str = str(random.randint(100000000, 999999999))

            if (self.account_number not in self.used_account_numbers):
                self.used_account_numbers.add(self.account_number)
                return self.account_number