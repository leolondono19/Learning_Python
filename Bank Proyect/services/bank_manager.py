from models.bank_account import BankAccount
from models.user import BankCustomer

class BankManager:
    def __init__(self, accounts_file: str, users_file: str) -> None:
        self.accounts_file = accounts_file
        self.users_file = users_file
        self.load_accounts()
        self.load_users()

    accounts_list: list[BankAccount] = []
    users_list: list[BankCustomer] = []
    #user_accounts: list[BankAccount] = []

    
    
    def log_in1(self, username: str) -> BankCustomer:
        for user in self.users_list:
            if username == user.username:
                return user

        raise ValueError("User not found.")

    
    
    

    def create_account(self, owner: BankCustomer, choose_type_account: str, choose_currency: str) -> None:

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

    
    
    #def load_user_accounts(self):