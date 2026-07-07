from models.bank_account import BankAccount

class AtmManager:
    def __init__(self) -> None:
        pass

    def log_in(self, username: str) -> BankAccount:
        for account in self.accounts_list:
            if username == account.owner.username:
                return account

        raise ValueError("Account not found.")