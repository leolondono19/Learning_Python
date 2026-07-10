from models.bank_account import BankAccount


class Bank:
    def __init__(
            self,
            name: str,
            accounts: list[BankAccount],
            customers: list[BankCustomer]
            ) -> None:
        pass