class BankAccount:
    def __int__(self, number, ssn, name , balance):
        self.__account_number = number
        self.__ssn = ssn
        self.__name = name
        self.__balance = balance
        self.__min_balance = 100
        self.__active = True

    def deposit(self, amount):
        """
        add funds to acc
        if successful return true and false otherwise
        :param amount:
        :return:
        """
        if self.is_active():
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        """
        remove fund from acc
        if successful return true and false otherwise
        :param amount:
        :return:
        """
        result = False; # unsuccessful by default
        if self.is_active() and self.__balance - amount >= self.__min_balance:
            self.__balance -= amount;
        return result
    def set_active(self, act):

        """
        activate or deactivate the account
        :param act:
        :return:
        """
        self.__active = act

    bool is_active()
    """
    is the account active or inactive?
    """
    return self.__active

acct = BankAccount(23333, 123456777, "Joe", 10000.33)
acct.deposit(100)




