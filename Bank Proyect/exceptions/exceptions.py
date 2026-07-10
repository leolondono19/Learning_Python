
class InvalidAmountException(Exception):
    def __init__(self, amount: float) -> None:
        super().__init__(
            f"The amount ({amount}) must be greater than zero."
        )

class InsufficientFundsException(Exception):
    def __init__(self, balance: float, amount: float) -> None:
        super().__init__(
            f"Insufficient founds. Balance: {balance} - Requested: {amount}"
        )
        
