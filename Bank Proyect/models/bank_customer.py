
from models.user import User
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.bank_account import BankAccount

class BankCustomer(User): 
    def __init__(
            self,
            username: str,
            password: str,
            first_name: str,
            last_name: str,
            age: int,
            phone: int,
            mail: str
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

    def __str__(self) -> str:
        return f"{self.username} | {self.first_name} | {self.last_name} | {self.age} | {self.phone} | {self.mail}"