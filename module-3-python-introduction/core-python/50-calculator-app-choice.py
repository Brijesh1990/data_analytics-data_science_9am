# create a function for additions
def add():
    a=int(input('Enter a values :'))
    b=int(input('Enter b values :'))
    c=a+b 
    print("Additions of numbers is :",c)

# create a function for substraction
def subs():
    a=int(input('Enter a values :'))
    b=int(input('Enter b values :'))
    c=a-b 
    print("Substractions of numbers is :",c)

# create a function for division
def dv():
    a=int(input('Enter a values :'))
    b=int(input('Enter b values :'))
    c=a/b 
    print("Divisions of numbers is :",c)

# create a function for multiplication
def mult():
    a=int(input('Enter a values :'))
    b=int(input('Enter b values :'))
    c=a*b 
    print("Multiplications of numbers is :",c)

# create a function for modulas
def mod():
    a=int(input('Enter a values :'))
    b=int(input('Enter b values :'))
    c=a%b 
    print("Modulas of numbers is :",c)

print("""
============select your choice============
1. select 1 for Additions
2. select 2 for Substractions
3. select 3 for Divisions
4. select 4 for Multiplications
5. select 5 for Modulas
6. select 6 for Exit      
      """)


while True:
    choice=int(input('Enter your choice :'))
    if choice==1:
        add()
    elif choice==2:
        subs()
    elif choice==3:
        dv()
    elif choice==4:
        mult()
    elif choice==5:
        mod()
    else:
        print('You have not selected a given choice please select one is proper as given')
        break
    
        