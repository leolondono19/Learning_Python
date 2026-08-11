import random
from models.user import User
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.bank_account import BankAccount
    from models.bank import Bank

class BankCustomer(User):
    used_customer_ids: set[str] = set()

    def __init__(
            self,
            username: str,
            password: str,
            first_name: str,
            last_name: str,
            age: int,
            phone: int,
            mail: str,
            customer_id: str | None = None
    ) -> None:
        super().__init__(
            username,
            password,
            first_name,
            last_name,
            age,
            phone,
            mail  
        )
        self.accounts: list["BankAccount"] = []
        self.banks: list["Bank"] = []
        if customer_id is None:
                    self.customer_id = self.__generate_customer_id()
        else:
            self.customer_id = customer_id
            BankAccount.used_account_ids.add(customer_id)

    def __str__(self) -> str:
        return f"{self.username} | {self.first_name} | {self.last_name} | {self.age} | {self.phone} | {self.mail}"

    def __generate_customer_id(self) -> str:
        while True:
            self.customer_id: str = str(random.randint(1000, 1999))

            if (self.customer_id not in self.used_customer_ids):
                self.used_customer_ids.add(self.customer_id)
                return f"{self.customer_id}" 