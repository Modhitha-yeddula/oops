class Test:
    g=70
    def __init__(self):
        self.a=10
        self.b=20
        Test.i=100
    def m1(self):
        self.c=30
    @classmethod
    def m2(cls):
        cls.e=50
        Test.h=80

t1=Test()
t1.m1()
print(t1.__dict__)
t2=Test()
t2.d=40
Test.f=60
t2.m2()
print(t2.__dict__)
print(Test.__dict__)





