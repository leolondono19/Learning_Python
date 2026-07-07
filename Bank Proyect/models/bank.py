from models.bank_account import BankAccount
from models.user import User

class Bank:
    def __init__(
            self,
            name: str,
            accounts: list[BankAccount],
            customers: list[User]
            ) -> None:
        pass