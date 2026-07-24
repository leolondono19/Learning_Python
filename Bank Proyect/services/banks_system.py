from models.bank import Bank
from repositories.banks_repository import AccountRepository

class BanksSystem:

    banks: list[Bank]

    def load_system() -> None:

