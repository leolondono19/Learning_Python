from models.bank_account import BankAccount
from models.user import User

class BankManager:
    def __init__(self, accounts_file: str, users_file: str) -> None:
        self.accounts_file = accounts_file
        self.users_file = users_file
        self.load_accounts()
        self.load_users()

    accounts_list: list[BankAccount] = []
    users_list: list[User] = []
    #user_accounts: list[BankAccount] = []

    def log_in(self, username: str) -> BankAccount:
        for account in self.accounts_list:
            if username == account.owner.username:
                return account

        raise ValueError("Account not found.")
    
    def log_in1(self, username: str) -> User:
        for user in self.users_list:
            if username == user.username:
                return user

        raise ValueError("User not found.")

    def create_user(self, username: str, name: str, surname: str, age: int, phone: int, mail: str, is_admin: str) -> None:
        user: User = User(username, name, surname, age, phone, mail)
        if is_admin == "y":
            admin_code: int = int(input("Enter the secret code:\n"))
            if admin_code == 1234:
                user.role = Role.ADMIN
            else: 
                return
        else:
            print("User successfully created!")
        
        self.users_list.append(user)
    
    def save_user(self):
        data: dict[str, Any] = { "users": [] }

        for user in self.users_list:
            data["users"].append(
                {
                    "username": user.username,
                    "name": user.name,
                    "surname": user.surname,
                    "age": user.age,
                    "phone": user.phone,
                    "mail": user.mail,
                    "role": user.role.value,
                }
            )

        with open(self.users_file, "w") as account_file:
            json.dump(data, account_file, indent=4)

    def load_users(self):
        if (not os.path.exists(self.users_file)):
            return

        with open(self.users_file, "r") as account_file:
            data = json.load(account_file)

            for user_data in data["users"]:
                user: User = User(
                    user_data["username"],
                    user_data["name"],
                    user_data["surname"],
                    user_data["age"],
                    user_data["phone"],
                    user_data["mail"],
                )

                self.users_list.append(user)

    def create_account(self, owner: User, choose_type_account: str, choose_currency: str) -> None:

        account: BankAccount = BankAccount(owner)

        if choose_type_account == "1":
            account.type_account = TypeBankAccount.SAVING_ACCOUNT
        elif choose_type_account == "2":
            account.type_account = TypeBankAccount.CHECKING_ACCOUNT

        if choose_currency == "1":
            account.currency = TypeBankCurrency.DOLARS
        elif choose_currency == "2":
            account.currency = TypeBankCurrency.BOLIVIANOS
        elif choose_currency == "3":
            account.currency = TypeBankCurrency.EUROS
        
        self.accounts_list.append(account)

    def save_account(self):
        data: dict[str, Any] = { "accounts": [] }

        for account in self.accounts_list:
            data["accounts"].append(
                {
                    "account number": account.account_number,
                    "owner": account.owner,
                    "type": account.type_account.value,
                    "balance": account.balance,
                    "currency": account.currency.value
                }
            )

        with open(self.accounts_file, "w") as account_file:
            json.dump(data, account_file, indent=4)

    def load_accounts(self):
        if (not os.path.exists(self.accounts_file)):
            return

        with open(self.accounts_file, "r") as account_file:
            data = json.load(account_file)

            for account_data in data["accounts"]:
                account: BankAccount = BankAccount(
                    account_data["owner"]
                )
                account.balance = account_data(["balance"])
                account.type_account = TypeBankAccount(account_data["type"])
                account.currency = TypeBankCurrency(account_data["currency"])

                self.accounts_list.append(account)
    
    #def load_user_accounts(self):