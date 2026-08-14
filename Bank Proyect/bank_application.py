from repositories.accounts_repository import AccountRepository
from repositories.banks_repository import BankRepository
from repositories.customer_repository import CustomerRepository
from repositories.bank_customer_repository import BankCustomerRepository
from services.authentication_service import AuthenticationService
from enums.account_type import TypeBankAccount
from enums.currency_type import TypeBankCurrency
from models.customer import Customer
from models.bank_customer import BankCustomer
from models.bank_account import BankAccount
from models.bank import Bank


bank_repository: BankRepository = BankRepository()
customer_repository: CustomerRepository = CustomerRepository()
authentication_service: AuthenticationService = AuthenticationService()
bank_customer_repository: BankCustomerRepository = BankCustomerRepository(customer_repository, bank_repository)
account_repository: AccountRepository = AccountRepository(bank_customer_repository)



#customer_list: list[BankCustomer] = customer_repository.load_customers()

#customer1: BankCustomer = BankCustomer("leolondono", "123", "leonee", "londono", 22, 67314221, "leoneelondono@gmail.com")
#customer2: BankCustomer = BankCustomer("simolondono", "123456", "simo0nee", "londono", 19, 63136523, "simoneelondono@gmail.com")
#account1: BankAccount = BankAccount(customer1, TypeBankAccount.SAVING_ACCOUNT, TypeBankCurrency.DOLARS)

#customers.append(customer1)
#customers.append(customer2)

#customer_repository.save_customer(customers)
#accounts.append(account1)
#account_repository.save_account(accounts)

"""
customer3: BankCustomer = BankCustomer("garyflorero", "00000", "gary", "florero", 50, 123456, "garyflorero@gmail.com")
account2: BankAccount = BankAccount(customer3, TypeBankAccount.SAVING_ACCOUNT, TypeBankCurrency.BOLIVIANOS)

customer_repository.customers.append(customer3)
customer_repository.save_customer()

account_repository.accounts.append(account2)
account_repository.save_account()
"""

bank: Bank = Bank("Banco Mercantil Santa Cruz", "BMSC" )
bank1: Bank = Bank("Banco Nacional de Bolivia", "BNB")

customer: Customer = Customer("leolondono", "1234", "Leonee", "Londono", 22, 67314221, "leolondono@gmail.com")

customer3: BankCustomer = BankCustomer(customer, bank)
account2: BankAccount = BankAccount(customer3, TypeBankAccount.SAVING_ACCOUNT, TypeBankCurrency.DOLARS)


bank_repository.banks.append(bank)
bank_repository.banks.append(bank1)
bank_repository.save_bank()

customer_repository.customers.append(customer3)
customer_repository.save_customer()

account_repository.accounts.append(account2)
account_repository.save_account()

"""

"""

#customer: BankCustomer = authentication_service.create_customer()
#customer_repository.customers.append(customer)
#customer_repository.save_customer()


for account in account_repository.accounts:
    print(account)

for customer in customer_repository.customers:
    print(customer)

