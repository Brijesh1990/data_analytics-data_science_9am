# create a function for loss
def loss():
    cost=int(input('Enter your cost price :'))
    sell=int(input('Enter your selling price :'))
    los=(cost-sell)
    # find loss in % 
    res=(los/cost)*100
    print("Total loss is :",res)
# create a function for profit
def profit():
    sell=int(input('Enter your selling price :'))
    cost=int(input('Enter your cost price :'))
    prof=(sell-cost)
    # find loss in % 
    res=(prof/sell)*100
    print("Total Profit by is :",res)
# create a function for totalrevenue
def totalrevenue():
    sell=int(input('Enter your selling price :'))
    cost=int(input('Enter your cost price :'))
    res=sell+cost 
    print("Total revenues is :",res)

"""print(\n
    select 1 for profit
    select 2 for loss
    select 3 for revenue
    elect 4 for exit app
)
"""

while True:
    choice=int(input("select your choice here : "))
    if choice==1:
        profit()
    elif choice==2:
        loss()
    elif choice==3:
        totalrevenue()
    else:
        print("you are selected invalid choice")
        break