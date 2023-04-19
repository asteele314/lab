class Account:
    """
    A class representing details for an Account object.
    """
    def __init__(self, name: str) -> None:
        """
        This sets the default values for each Account object.
        :param name: The name of each Account object.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> None:
        """
        This increments the account balance by the amount.
        :param amount: The amount deposited to the account.
        :return: The Boolean value True if the account transaction is successful and False if the transaction is unsuccessful.
        """
        amount = float(amount)
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> None:
        """
        This decrements the account balance by the amount.
        :param amount: The amount withdrawn from the account.
        :return: The Boolean value True if the account transaction is successful and False if the transaction is unsuccessful.
        """
        amount = float(amount)
        if amount <= 0:
            return False
        elif amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        This returns the account balance.
        :return: The account balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        This returns the account name.
        :return: The account name.
        """
        return self.__account_name
