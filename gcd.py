def find_gcd(a,b):
     while b:
      a,b=b,a%b
     return(a)

    
n1=int(input("Enter the 1 no:"))
n2=int(input("Enter the 2 no:"))
GCD=find_gcd(n1,n2)
print("The3 GCD of",n1,"and",n2,GCD,)
