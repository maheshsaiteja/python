n=int(input("Enter inches: "))
class convert:
    def inchtofeets(self,n):
        self.feets=n/12
    def display(self):
        print("Feets:",self.feets)
c=convert()
c.inchtofeets(n)
c.display()