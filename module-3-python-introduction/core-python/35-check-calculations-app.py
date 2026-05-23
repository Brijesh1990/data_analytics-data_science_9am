# w.a.p to check conditionaly if user input 2 values take input from users if user select 1 performed additions, 2 performed substraction , 3 performed multiplications , 4 performed subtsraction , 5 performed divisiond if select another values its returned not able to calculate

a=int(input('Enter a values :'))
b=int(input('Enter a values :'))
res=int(input("Select number for Calculations :"))

if res==1:
    print("Additions of numbers :",a+b)
elif res==2:
    print("Substractions of numbers :",a-b)
elif res==3:
    print("Multiplications of numbers :",a*b)
elif res==4:
    print("Modulas of numbers :",a%b)
elif res==5:
    print("Divisions of numbers :",a/b)

else:
    print("Not performed select  as instructed numbers")