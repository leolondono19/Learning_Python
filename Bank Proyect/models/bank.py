#from models.bank_account import BankAccount
import random


class Bank:
    used_bank_ids: set[str] = set()

    def __init__(
            self,
            name: str,
            bank_code: str,
            bank_id: int | None = None
        ) -> None:

        if bank_id is None:
            self.bank_id = self.__generate_bank_id()
        else:
            self.bank_id = str(bank_id)
            self.used_bank_ids.add(self.bank_id)
        self.__name = name
        self.__bank_code = bank_code

    @property
    def name(self) -> str:
        return self.__name

    @property
    def bank_code(self) -> str:
        return self.__bank_code

    def __generate_bank_id(self) -> str:
        while True:
            self.bank_id: str = str(random.randint(1000, 1999))

            if (self.bank_id not in self.used_bank_ids):
                self.used_bank_ids.add(self.bank_id)
                return f"{self.bank_id}"