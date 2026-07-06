class User:
    def __init__(
            self,
            username: str,
            name: str,
            surname: str,
            age: int,
            phone: int,
            mail: str
            ) -> None:
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.mail = mail
        self.role = Role.CUSTOMER