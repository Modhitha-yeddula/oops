class Parent:
    def common(self):
        print("Parent method")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()
c1.common()
c2.common()
