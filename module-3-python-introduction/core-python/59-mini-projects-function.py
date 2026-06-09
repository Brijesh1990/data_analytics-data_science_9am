# ----------------------print action what you want to print ...............
print("""\n
      
      1. select 1 for additions 
      2. select 2 for substractions
      3. select 3 for multiplications
      4. select 4 for divisions
      5. select 5 for modulas 
      6. select 6 for programmes exit
      
      """)

# create each function for calculations 
def add(a,b):
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    c=a+b 
    print("Additions of numbers is :",c)
def subs(a,b):
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    c=a-b 
    print("Substractions of numbers is :",c)
def mult(a,b):
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    c=a*b 
    print("Multiplications of numbers is :",c)
def dv(a,b):
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    c=a/b 
    print("Divisions of numbers is :",c)
def mod(a,b):
    a=int(input("Enter a values :"))
    b=int(input("Enter b values :"))
    c=a%b 
    print("Modulas  of numbers is :",c)    
while True:
    choice=int(input("Enter your choices : "))
    # select choices on conditions based 
    if choice ==1:
        # call your function
        add("a","b")
    elif choice==2:
         # call your function
        subs("a","b")
    elif choice==3:
         # call your function
        mult("a","b")
    elif choice==4:
         # call your function
        dv("a","b")
    elif choice==5:
         # call your function
        mod("a","b")
    elif choice==6:
        print("You are selected wrong choices")
        break