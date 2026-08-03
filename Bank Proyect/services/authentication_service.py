from models.user import User
from models.bank_customer import BankCustomer
from services.display_service import clear_display
from services.display_service import pause_display


class AuthenticationService:
    def __init__(self) -> None:
        pass

    def create_customer(self) -> BankCustomer:
        print("Complete your register:\n")
        username: str = input("Please insert your username (This will use for your bank account)\n")
        first_name: str = input("Please insert your name\n")
        last_name: str = input("Please insert your last name\n")
        age: int = int(input("Please insert your age\n"))
        phone: int = int(input("Please insert your phone\n"))
        mail: str = input("Please insert your mail\n")
        clear_display()
        password: str = input("Please create a strong password\n")

        customer: BankCustomer = BankCustomer(username, password, first_name, last_name, age, phone, mail)
        print("Customer succesfully created!!")
        return customer
    