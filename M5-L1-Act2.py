class account:
    def __init__(self,bal ,acc ):
        self.balance = bal
        self.account_no = acc
    def debit(self,amount):
        self.balance = self.balance - amount
        print("Rs",amount,"from account no", self.account_no,"was debited")
        print("total balance", self.get_bal())
    def credit(self,amount):
        self.balance = self.balance + amount
        print("Rs",amount,"from account no", self.account_no,"was credited")
        print("total balance", self.get_bal())
    def get_bal(self):
        return self.balance

acc1 =account(10000,12000)
acc1.debit(3000)