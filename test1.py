class Parent:
    def m1(self):
        print("ParentClass method")
    def m2(self):
        print("ParentClass method 2")
class Child(Parent):
    def m3(self):
        print("ChildClass method")

c1=Child()
c1.m1()
print(c1)
c1.m2()
c1.m3()