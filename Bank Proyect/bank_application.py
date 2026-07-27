from repositories.accounts_repository import AccountRepository
from repositories.banks_repository import BankRepository
from repositories.customer_repository import CustomerRepository
from models.bank import Bank
from models.bank_account import BankAccount
from models.bank_customer import BankCustomer
from enums.account_type import TypeBankAccount
from enums.currency_type import TypeBankCurrency


account_repository: AccountRepository = AccountRepository()
bank_repository: BankRepository = BankRepository()
customer_repository: CustomerRepository = CustomerRepository()

#customer_list: list[BankCustomer] = customer_repository.load_customers()

#customer1: BankCustomer = BankCustomer("leolondono", "123", "leonee", "londono", 22, 67314221, "leoneelondono@gmail.com")
#customer2: BankCustomer = BankCustomer("simolondono", "123456", "simo0nee", "londono", 19, 63136523, "simoneelondono@gmail.com")
#account1: BankAccount = BankAccount(customer1, TypeBankAccount.SAVING_ACCOUNT, TypeBankCurrency.DOLARS)

#customers.append(customer1)
#customers.append(customer2)

#customer_repository.save_customer(customers)
#accounts.append(account1)
#account_repository.save_account(accounts)

customers: list[BankCustomer] = customer_repository.load_customers()
accounts: list[BankAccount] = account_repository.load_accounts(customers)

for customer in customers:
    print(customer)

for account in accounts:
    print(account)
"""
accounts = account_repository.load_accounts()
for account in accounts:
    print(account)
"""
