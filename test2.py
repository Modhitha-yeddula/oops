class GP:
    def m1(self):
        print("GP method")
    def m2(self):
        print("GP method 2")    
class Parent(GP):
    def m3(self):
        print("Parent method")
class Child(Parent):
    def m4(self):
        print("Child method")
c1=Child()
print(c1.m1)
