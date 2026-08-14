import random
from models.user import User


class Customer(User):
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
            customer_id: int | None = None
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
        if customer_id is None:
            self.customer_id = self.__generate_customer_id()
        else:
            self.customer_id = str(customer_id)
            self.used_customer_ids.add(self.customer_id)


    def __str__(self) -> str:
        return f"{self.username} | {self.first_name} | {self.last_name} | {self.age} | {self.phone} | {self.mail}"

    def __generate_customer_id(self) -> str:
        while True:
            self.customer_id: str = str(random.randint(1000, 1999))

            if (self.customer_id not in self.used_customer_ids):
                self.used_customer_ids.add(self.customer_id)
                return f"{self.customer_id}" 