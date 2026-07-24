
from models.user import User
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.bank_account import BankAccount

class BankCustomer(User): #TODO: should inherit from user
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
       
        self.accounts = list["BankAccount"] 