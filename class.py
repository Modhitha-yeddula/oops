""" class MyClass:
    x=10
p=MyClass()
print(p.x) """
class MyClass:
    def __init__(self):
        self.x = 5

p = MyClass()
print(p.x)
print(type(p))
