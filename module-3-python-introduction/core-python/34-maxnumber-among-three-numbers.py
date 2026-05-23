n1=int(input('Enter N1 numbers :'))
n2=int(input('Enter N2 numbers :'))
n3=int(input('Enter N3 numbers :'))

if n1>n2 and n1>n3:
    print("N1 is max numbers")
elif n2>n1 and n2>n3:
    print("N2 is max numbers")
elif n3>n2 and n3>n1:
    print("N3 is max numbers")
else:
    print("something went wrong while checked")