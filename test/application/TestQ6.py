import unittest
from application.BankAccount import *


class BankAccountTest(unittest.TestCase):
    def test_creation(self):
        b = BankAccount(123)
        self.assertIsNotNone(b)
        self.assertEqual(0, b.get_balance())

        b = BankAccount(456, 100)
        self.assertIsNotNone(b)
        self.assertEqual(100, b.get_balance())

    def test_credit(self):
        b = BankAccount(123)
        self.assertEqual(0, b.get_balance())

        b.credit(78)
        self.assertEqual(78, b.get_balance())

        b.credit(2)
        self.assertEqual(80, b.get_balance())

    def test_debit(self):
        b = BankAccount(123)
        self.assertEqual(0, b.get_balance())

        b.debit(10)
        self.assertEqual(-10, b.get_balance())

        b.credit(15)
        self.assertEqual(5, b.get_balance())

        b.debit(2)
        self.assertEqual(3, b.get_balance())

    def test_get_id(self):
        b = BankAccount(123)
        self.assertEqual(123, b.get_id())

    def test_get_balance(self):
        b = BankAccount(123)
        self.assertEqual(0, b.get_balance())

        b = BankAccount(123, 345)
        self.assertEqual(345, b.get_balance())

        b.credit(5)
        self.assertEqual(350, b.get_balance())

        b.debit(10)
        self.assertEqual(340, b.get_balance())


class SavingAccountTest(unittest.TestCase):
    def test_creation(self):
        b = SavingAccount(123)
        self.assertIsNotNone(b)
        self.assertEqual(0, b.get_balance())

        b = SavingAccount(123)
        self.assertIsNotNone(b)
        self.assertEqual(0, b.get_balance())

        b = SavingAccount(456, 100)
        self.assertIsNotNone(b)
        self.assertEqual(100, b.get_balance())

    def test_credit(self):
        b = SavingAccount(123)
        self.assertEqual(0, b.get_balance())

        b.credit(78)
        self.assertEqual(78, b.get_balance())

        b.credit(2)
        self.assertEqual(80, b.get_balance())

    def test_debit(self):
        b = SavingAccount(123)
        self.assertEqual(0, b.get_balance())

        b.debit(10)
        self.assertEqual(-10, b.get_balance())

        b.credit(15)
        self.assertEqual(5, b.get_balance())

        b.debit(2)
        self.assertEqual(3, b.get_balance())

    def test_get_id(self):
        b = SavingAccount(123)
        self.assertEqual(123, b.get_id())

    def test_get_balance(self):
        b = SavingAccount(123)
        self.assertEqual(0, b.get_balance())

        b = SavingAccount(123, 345)
        self.assertEqual(345, b.get_balance())

        b.credit(5)
        self.assertEqual(350, b.get_balance())

        b.debit(10)
        self.assertEqual(340, b.get_balance())

    def test_pay_interest(self):
        b = SavingAccount(123)
        self.assertEqual(0, b.get_balance())

        b.credit(100)
        self.assertEqual(100, b.get_balance())

        b.pay_interest(0.15)
        self.assertEqual(115, b.get_balance())


class LoyaltyAccountTest(unittest.TestCase):
    def test_creation(self):
        b = LoyaltyAccount(123)
        self.assertIsNotNone(b)
        self.assertEqual(0, b.get_balance())

        b = LoyaltyAccount(123)
        self.assertIsNotNone(b)
        self.assertEqual(0, b.get_balance())

        b = LoyaltyAccount(456, 100)
        self.assertIsNotNone(b)
        self.assertEqual(100, b.get_balance())

    def test_credit(self):
        b = LoyaltyAccount(123)
        self.assertEqual(0, b.get_balance())

        b.credit(78)
        self.assertEqual(78, b.get_balance())

        b.credit(2)
        self.assertEqual(80, b.get_balance())

    def test_debit(self):
        b = LoyaltyAccount(123)
        self.assertEqual(0, b.get_balance())

        b.debit(10)
        self.assertEqual(-10, b.get_balance())

        b.credit(15)
        self.assertEqual(5, b.get_balance())

        b.debit(2)
        self.assertEqual(3, b.get_balance())

    def test_get_id(self):
        b = LoyaltyAccount(123)
        self.assertEqual(123, b.get_id())

    def test_get_balance(self):
        b = LoyaltyAccount(123)
        self.assertEqual(0, b.get_balance())

        b = LoyaltyAccount(123, 345)
        self.assertEqual(345, b.get_balance())

        b.credit(5)
        self.assertEqual(350, b.get_balance())

        b.debit(10)
        self.assertEqual(340, b.get_balance())

    def test_pay_and_bonus(self):
        b = LoyaltyAccount(123)
        self.assertEqual(0, b.get_balance())

        b.credit(100)
        self.assertEqual(100, b.get_balance())
        self.assertEqual(1, b.get_bonus())

        b.credit(200)
        self.assertEqual(300, b.get_balance())
        self.assertEqual(3, b.get_bonus())

        b.pay_bonus()
        self.assertEqual(303, b.get_balance())
        self.assertEqual(0, b.get_bonus())


class TestQ6(unittest.TestCase):
    def test_bank_account_insertion(self):
        m = AccountManager()
        m.add(BankAccount(123))
        m.add(BankAccount(456))
        m.add(BankAccount(789))
        self.assertEqual(3, m.length)
        self.assertEqual("id: 123\nbalance: 0", str(m.find(123)))

    def test_saving_account_insertion(self):
        m = AccountManager()
        m.add(SavingAccount(123))
        m.add(SavingAccount(456))
        m.add(SavingAccount(789))
        self.assertEqual(3, m.length)
        self.assertEqual("id: 456\nbalance: 0", str(m.find(456)))

    def test_loyalty_account_insertion(self):
        m = AccountManager()
        m.add(LoyaltyAccount(123))
        m.add(LoyaltyAccount(456))
        m.add(LoyaltyAccount(789))
        self.assertEqual(3, m.length)
        self.assertEqual("id: 789\nbalance: 0", str(m.find(789)))

    def test_credit_in_account(self):
        m = AccountManager()
        m.add(BankAccount(123))
        m.add(SavingAccount(456))
        m.add(LoyaltyAccount(789))
        self.assertEqual(3, m.length)

        m.credit_account(123, 59)
        m.credit_account(456, 33)
        m.credit_account(789, 128)

        self.assertEqual(59, m.get_balance_account(123))
        self.assertEqual(33, m.get_balance_account(456))
        self.assertEqual(128, m.get_balance_account(789))

    def test_debit_in_account(self):
        m = AccountManager()
        m.add(BankAccount(123, 100))
        m.add(SavingAccount(456, 100))
        m.add(LoyaltyAccount(789, 100))
        self.assertEqual(3, m.length)

        m.debit_account(123, 60)
        m.debit_account(456, 100)
        m.debit_account(789, 170)

        self.assertEqual(40, m.get_balance_account(123))
        self.assertEqual(0, m.get_balance_account(456))
        self.assertEqual(-70, m.get_balance_account(789))

    def test_balance_account(self):
        m = AccountManager()
        m.add(BankAccount(123, 10))
        m.add(SavingAccount(456, -34))
        m.add(LoyaltyAccount(789, 99))
        self.assertEqual(3, m.length)

        self.assertEqual(10, m.get_balance_account(123))
        self.assertEqual(-34, m.get_balance_account(456))
        self.assertEqual(99, m.get_balance_account(789))

    def test_bonus_loyalty_account(self):
        m = AccountManager()
        m.add(LoyaltyAccount(123, 876))
        m.add(BankAccount(456, 998))

        m.credit_account(123, 44)
        m.credit_account(456, 150)

        self.assertEqual(0.44, m.get_bonus_account(123))
        self.assertIsNone(m.get_bonus_account(456))

    def test_transfer(self):
        m = AccountManager()
        m.add(BankAccount(123, 100))
        m.add(LoyaltyAccount(456, 15))
        m.add(SavingAccount(789, 75))

        m.transfer_account(123, 456, 50)
        self.assertEqual(50, m.get_balance_account(123))
        self.assertEqual(65, m.get_balance_account(456))

        m.transfer_account(789, 123, 20)
        self.assertEqual(55, m.get_balance_account(789))
        self.assertEqual(70, m.get_balance_account(123))

    def test_pay_interest_saving_account(self):
        m = AccountManager()
        m.add(SavingAccount(123, 100))
        m.add(BankAccount(456, 80))
        self.assertEqual(100, m.get_balance_account(123))
        self.assertEqual(80, m.get_balance_account(456))

        m.pay_interest_account(123, 0.5)
        self.assertEqual(150, m.get_balance_account(123))

        m.pay_interest_account(456, 0.5)
        self.assertEqual(80, m.get_balance_account(456))

    def test_pay_bonus_loyalty_account(self):
        m = AccountManager()
        m.add(LoyaltyAccount(123, 150))
        m.add(BankAccount(456, 200))
        self.assertEqual(150, m.get_balance_account(123))
        self.assertEqual(200, m.get_balance_account(456))

        m.credit_account(123, 100)
        m.pay_bonus_account(123)
        self.assertEqual(251, m.get_balance_account(123))

        m.credit_account(456, 100)
        self.assertEqual(300, m.get_balance_account(456))

    def test_remove_account(self):
        m = AccountManager()
        m.add(BankAccount(123))
        m.add(SavingAccount(456))
        m.add(LoyaltyAccount(789))
        m.add(LoyaltyAccount(101112))
        m.add(LoyaltyAccount(131415))
        self.assertEqual(5, m.length)

        m.remove(123)
        self.assertEqual(4, m.length)
        self.assertIsNone(m.find_account(123))

        m.remove(131415)
        self.assertEqual(3, m.length)
        self.assertIsNone(m.find_account(131415))

        m.remove(789)
        self.assertEqual(2, m.length)
        self.assertIsNone(m.find_account(789))

    def test_show_account_status(self):
        m = AccountManager()
        m.add(BankAccount(123, -32))
        m.add(SavingAccount(456, 55))
        m.add(LoyaltyAccount(789, 99))
        m.add(BankAccount(131415, 776))
        self.assertEqual(4, m.length)

        self.assertEqual("id: 131415\n" +
                         "balance: 776\n" +
                         "id: 789\n" +
                         "balance: 99\n" +
                         "id: 456\n" +
                         "balance: 55\n" +
                         "id: 123\n" +
                         "balance: -32\n", str(m))

if __name__ == '__main__':
    unittest.main()