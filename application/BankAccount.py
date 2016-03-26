from datastructure.list.LinkedList import LinkedList


class BankAccount(object):
    def __init__(self, id_account, balance=0):
        self.__id_account = id_account
        self.__balance = balance

    def credit(self, value):
        self.__balance += value

    def debit(self, value):
        self.__balance -= value

    def get_id(self):
        return self.__id_account

    def get_balance(self):
        return self.__balance

    def __eq__(self, other):
        if self.__id_account == other:
            return True
        return False

    def __str__(self):
        return "id: " + str(self.__id_account) + "\nbalance: " + str(self.__balance)


class SavingAccount(BankAccount):
    def __init__(self, id_account, balance=0):
        super(SavingAccount, self).__init__(id_account, balance)

    def pay_interest(self, interest):
        return self.credit(self.get_balance() * interest)


class LoyaltyAccount(BankAccount):
    def __init__(self, id_account, balance=0, bonus=0):
        super(LoyaltyAccount, self).__init__(id_account, balance)
        self.__bonus = bonus

    def credit(self, value):
        super(LoyaltyAccount, self).credit(value)
        self.__bonus += value * 0.01

    def pay_bonus(self):
        super(LoyaltyAccount, self).credit(self.__bonus)
        self.__bonus = 0

    def get_bonus(self):
        return self.__bonus


class AccountManager(LinkedList):
    def credit_account(self, id_account, value):
        node = self.find_account(id_account)
        if node is not None:
            return node.credit(value)
        return None

    def debit_account(self, id_account, value):
        node = self.find_account(id_account)
        if node is not None:
            return node.debit(value)
        return None

    def find_account(self, id_account):
        father, node = self.find_node(id_account)
        if node is not None:
            return node.value
        return None

    def remove_account(self, id_account):
        pass

    def get_balance_account(self, id_account):
        node = self.find_account(id_account)
        if node is not None:
            return node.get_balance()
        return None

    def get_bonus_account(self, id_account):
        node = self.find_account(id_account)
        if node is not None and isinstance(node, LoyaltyAccount):
            return node.get_bonus()
        return None

    def transfer_account(self, source, target, value):
        account_source = self.find_account(source)
        account_target = self.find_account(target)
        if account_source is not None and account_target is not None:
            account_source.debit(value)
            account_target.credit(value)
        return None

    def pay_interest_account(self, id_account, interest):
        node = self.find_account(id_account)
        if node is not None and isinstance(node, SavingAccount):
            node.pay_interest(interest)
            return node.get_balance()
        return None

    def pay_bonus_account(self, id_account):
        node = self.find_account(id_account)
        if node is not None and isinstance(node, LoyaltyAccount):
            node.pay_bonus()
            return node.get_balance()
        return None

    def __str__(self):
        result_string = ""
        it_node = self.head
        if it_node is not None:
            result_string += str(it_node.value) + "\n"
            while it_node.next is not None:
                result_string += str(it_node.next.value) + "\n"
                it_node = it_node.next
        return result_string
