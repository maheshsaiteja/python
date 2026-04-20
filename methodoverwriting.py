class A:
    def show(self):
        print("I Am From Parent Class")
class B(A):
    def  show(self):
        print("I Am From Child Class")
s=B() 
s.show()       