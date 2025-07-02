class Account:
    def __init__(self,id,name,amount):
        self.id=id
        self.name=name
        self.acc_bal=amount
    def deposit_amount(self,amount):
        self.acc_bal=self.acc_bal+amount
    def withdrawl(self,amount):
        self.acc_bal=self.acc_bal-amount
    def get_bal(self):
        self.acc_bal=self.acc_bal-500
a1=Account(101,"rahul",10000)
a1.deposit_amount(1000)
print(a1.__dict__)
a2=Account(102,"suresh",20000)
a2.deposit_amount(2000)
print(a2.__dict__)
a2=Account(102,"sonia",15000)
a2.deposit_amount(2500)
print(a2.__dict__)
a1.withdrawl(2000)
print(a1.__dict__)

print("your bal:", a1.get_bal())