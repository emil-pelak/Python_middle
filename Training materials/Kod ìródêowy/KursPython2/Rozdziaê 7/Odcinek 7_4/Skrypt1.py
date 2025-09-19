class MyCustomException(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code


def divide_numbers(a, b):
    if b == 0:
        raise MyCustomException('Division by zero is not allowed!')
    else:
        return a / b


try:
    result = divide_numbers(10, 0)
    raise MyCustomException("Something went wrong.", error_code=500)
except MyCustomException as ex:
    print("An error occurred:", str(ex), type(ex).__name__)
    print("Error code:", ex.error_code)


class InsufficientFundsException(Exception):
    def __init__(self, account_number, balance, withdrawal_amount):
        self.account_number = account_number
        self.balance = balance
        self.withdrawal_amount = withdrawal_amount
        super().__init__(
            f"Insufficient funds in account {account_number}. Balance: {balance}. Attempted withdrawal: {withdrawal_amount}.")


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException(self.account_number, self.balance,
                                             amount)
        self.balance -= amount


try:
    account = BankAccount('123456789', 1000)
    account.withdraw(1500)
except InsufficientFundsException as ex:
    print("Error:", str(ex))
