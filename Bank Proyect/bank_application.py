from repositories.accounts_repository import AccountRepository
from repositories.banks_repository import BankRepository
from repositories.customer_repository import CustomerRepository
from models.bank import Bank
from models.bank_account import BankAccount
from models.bank_customer import BankCustomer
from enums.account_type import TypeBankAccount
from enums.currency_type import TypeBankCurrency

accounts: list[BankAccount] = []

account_repository: AccountRepository = AccountRepository()
bank_repository: BankRepository = BankRepository()
customer_repository: CustomerRepository = CustomerRepository()

#customer_list: list[BankCustomer] = customer_repository.load_customers()

customer1: BankCustomer = BankCustomer("leolondono", "123", "leonee", "londono", 22, 67314221, "leoneelondono@gmail.com")
account1: BankAccount = BankAccount(customer1, TypeBankAccount.SAVING_ACCOUNT, TypeBankCurrency.DOLARS)

#accounts.append(account1)
#account_repository.save_account(accounts)

accounts = account_repository.load_accounts()
for account in accounts:
    print(account)
"""

"""
