

class User: 
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
        self.__username = username
        self.__password = password
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__phone = phone
        self.__mail = mail

    @property
    def username(self) -> str:
        return self.__username
    
    @property
    def password(self) -> str:
        return self.__password
    
    @property
    def first_name(self) -> str:
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        return self.__last_name
    
    @property
    def age(self) -> int:
        return self.__age
    
    @property
    def phone(self) -> int:
        return self.__phone