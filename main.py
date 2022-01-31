class BikeshopAmit:
    def __init__(self, stock):
        self.stock = stock
    def dis(self):
        print(self.stock)
    def renforbike(self, q):
        if q>=self.stock:
            print("Value must be greate then 0")
        elif q>self.stock:
            print(self.stock,"is my stock.")
        else:
            self.stock = self.stock-q
            print("total Price: ", q*100)
            print("total Bikes: ", self.stock)
while True:
    obj = BikeshopAmit(1000)
    uc = int(input('''Enter You choice
    1. Display Bike Stock. 
    2. Bike on Rent.
    3. Exit'''))
    if uc == 1:
        obj.dis()
    elif uc == 2:
        n = int(input("Enter Qunatity: "))
        obj.renforbike(n)
    else:
        break
