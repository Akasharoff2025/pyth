
class customer:
    def getData(self,name,accno,acctype,balance):
        self.name=name
        self.accno=accno
        self.acctype=acctype
        self.balance=balance
    def displayCustomer(self):
        print("Customer Name:",self.name)
        print("Account number",self.accno)
        print("Type of account",self.acctype)
        print("Balance",self.balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdrawal(self,amount):
        if self.balance-amount<0:
            print("Insufficient balance")
        else:self.balance=self.balance-amount
ch=0
while(ch!=5):
    print("1.New Customer")
    print("2.Deposit")
    print("3.withdrawl")
    print("4.Display")
    print("5.Exit")
    ch=int(input("Enter your choice:"))
    if (ch==1):
        obj=customer()
        n=input("Enter name:")
        no=int(input("Enter Account number:"))
        t=input("Enter Account Type (SB/c):")
        b=int(input("Enter the Amount:"))
        obj.getData(n,no,t,b)
    if (ch==2):
        b=int(input("Enter the amount to be deposited:"))
        obj.deposit(b)
    if (ch==3):
        b=int(input("Enter the amount to be withdrawn:"))
        obj.withdrawal(b)
    if (ch==4):
        obj.displayCustomer()
    else:
        print("Program Terminated")
          
           


















    
    
        
        
    
