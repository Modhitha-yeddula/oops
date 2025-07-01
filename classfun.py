class Account:
    def open_account(self,name):
        print("Account opened: ",name)
    def deposit_amount(self,amount):
        print("amount deposited: ",amount)
    def withdrawl(self,amount):
        print("withdrawl amount: ",amount)
    def get_bal(self):
        print("the balance is")
    def close_acc(self):
        print("account closed")

a1=Account()
a1.open_account("rahul")
a1.deposit_amount(10000)
a1.withdrawl(5000)
a1.get_bal()
a1.close_acc()

