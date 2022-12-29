class Computer:
    def __init__(self,stock):
        self.stock=stock
    def display(self):
        print("TOTAL COMPUTER AVAILABELE IN STOCK \n",self.stock)
    def rent(self,q):
        if q<=0:
            print("Enter the Amount greater then Zero")
        elif q>self.stock:
            print("Enter The Value that Less Then Stock")
        else:
            print("YOUR TOTAL AMOUNT OF RENT IS  \n",q*200)
            print("AVAILABLE STOCKS IN STUDIO",self.stock-q)
            print("THANK YOU FOR RENTING ",q," COMPUTER FROM US")
while True:
    print("*****CREATED BY FATHERPRINCE *****")
    print("*****1COMPUTER RENT IS 200rupee PER HOUR****")
    ob=Computer(50)
    
    c=int(input('''
    1 Show Stock
    2 Rent Computer
    3 Exit
'''))   
    if c==1:
        ob.display()
    elif c==2:
        q=int(input("ENTER THE QUANTITY OF COMPUTER\n"))
        ob.rent(q)
    else:
        break
        
                 
