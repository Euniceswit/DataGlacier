import pickle

class Employee:

    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print('ENO:{}, ENAME:{}, ESAL:{}, EADDR:{}'.format(self.eno,self.ename,self.esal,self.eaddr))

emp = Employee(120, 'Eunice', 4500, 'Aberdeen')

with open('emp.pkl', 'wb') as f:
    pickle.dump(emp, f)
    print("Pickling completed")


with open('emp.pkl', 'rb') as f:
     obj = pickle.load(f)
     print("Un-Pickling completed")
     obj.display()