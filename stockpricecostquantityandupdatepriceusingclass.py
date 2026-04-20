n = input("Enter stock name: ")
q = int(input("Enter quantity: "))
p = float(input("Enter price for one stock: "))
up = float(input("Enter updated price: "))
uq = int(input("Enter updated quantity: "))

class Stock:
    def details(self, n, q, p):
        self.name = n
        self.quantity = q
        self.price = p
        self.totalcost = q * p

    def currentdetails(self, up, uq):
        self.updatedprice = up
        self.updatedquantity = uq

    def updateafterprice(self):
        self.updatedtotal = self.updatedquantity * self.updatedprice

    def display(self):
        print("Stock name:", self.name)
        print("Old total cost:", self.totalcost)
        print("Updated total cost:", self.updatedtotal)

s = Stock()
s.details(n, q, p)
s.currentdetails(up, uq)
s.updateafterprice()
s.display()