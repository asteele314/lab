import pytest
from account import *


account1 = Account('name')


def test_init():
    assert account1.__account_name == 'name'
    assert account1.__account_balance == 0


def test_deposit():
    assert account1.deposit(-10) is False
    assert account1.deposit(0) is False
    assert account1.deposit(100) is True


def test_withdraw():
    assert account1.withdraw(-10) is False
    assert account1.withdraw(0) is False
    assert account1.withdraw(10) is True
