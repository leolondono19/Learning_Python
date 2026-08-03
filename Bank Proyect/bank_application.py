from repositories.accounts_repository import AccountRepository
from repositories.banks_repository import BankRepository
from repositories.customer_repository import CustomerRepository
from services.authentication_service import AuthenticationService
from models.bank_customer import BankCustomer

authentication_service: AuthenticationService = AuthenticationService()
customer_repository: CustomerRepository = CustomerRepository()
account_repository: AccountRepository = AccountRepository(customer_repository)
bank_repository: BankRepository = BankRepository()


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
"""

"""

#customer: BankCustomer = authentication_service.create_customer()
#customer_repository.customers.append(customer)
#customer_repository.save_customer()


for account in account_repository.accounts:
    print(account)

for customer in customer_repository.customers:
    print(customer)

