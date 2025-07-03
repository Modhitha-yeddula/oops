class Employee:
    company_name="TCS"
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal
e1=Employee(101,"rahul",30000)
e2=Employee(102,"sonia",55000)
e3=Employee(103,"priya",45000)
print(Employee.__dict__)
print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)       