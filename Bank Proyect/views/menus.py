from enums.account_type import TypeBankAccount
from enums.currency_type import TypeBankCurrency
            


def show_Atm_menu() -> None:
    print("\n----Welcome to your ATM operations----") 
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("5. Exit")

def show_bank_menu() -> None:
    print("\n----Welcome to your BANK----")
    print("1. Create User")
    print("2. Create Account")
    print("3. ATM")
    print("4. Delete a task")
    print("5. Show accounts")
    print("6. Exit")

def show_type_account_menu() -> None:
    print(f"1.- {TypeBankAccount.SAVING_ACCOUNT.value}")
    print(f"1.- {TypeBankAccount.CHECKING_ACCOUNT.value}")

def show_currency() -> None:
    print(f"1.- {TypeBankCurrency.DOLARS.value}")
    print(f"1.- {TypeBankCurrency.BOLIVIANOS.value}")
    print(f"1.- {TypeBankCurrency.EUROS.value}")