class Investment:
    def __int__(self, principal, interest, rate):
        self._principal = principal
        self._interest = interest
        self._rate = 5.12 / 100

    def value_before(self, principal):
        principal = 0.00

    def value_after(self, principal, rate):
        interest = principal * rate


total = Investment
total.value_after(222, 22)
