import random

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
    
    def _generate_account_number(self) -> str:
        while True:
            self.account_number: str = str(random.randint(100000000, 999999999))

            if (self.account_number not in self.used_account_numbers):
                self.used_account_numbers.add(self.account_number)
                return self.account_number