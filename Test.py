class Test:
    def __init__(self):
        print("constructor is a special method")
    def __init__(self):
        print("instance method")
    def m2(cls):
        print("class method")
    def m3(self):
        print("static method")
t=Test()
