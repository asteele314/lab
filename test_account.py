from account import *


class Test:
    def setup_method(self):
        self.account1 = Account('Name1')
    
    
    def teardown_method(self):
        del self.account1
    
    
    def test_init(self):
        assert self.account1.get_name() == 'Name1'
        assert self.account1.get_balance() == 0
    
    
    def test_deposit(self):
        assert self.account1.deposit(-10) is False
        assert self.account1.get_balance() == 0
        assert self.account1.deposit(0) is False
        assert self.account1.get_balance() == 0
        assert self.account1.deposit(10) is True
        assert self.account1.get_balance() == 10
        assert self.account1.deposit(107.5) is True
        assert self.account1.get_balance() == 117.5
        self.account1.withdraw(117.5)
    
    
    def test_withdraw(self):
        self.account1.deposit(100)
        assert self.account1.withdraw(-25) is False
        assert self.account1.get_balance() == 100
        assert self.account1.withdraw(0) is False
        assert self.account1.get_balance() == 100
        assert self.account1.withdraw(250) is False
        assert self.account1.get_balance() == 100
        assert self.account1.withdraw(20) is True
        assert self.account1.get_balance() == 80
        assert self.account1.withdraw(37.5) is True
        assert self.account1.get_balance() == 42.5
        
