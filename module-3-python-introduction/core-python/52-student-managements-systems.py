# create an students managements-systems 
# create a function for add students
def add_student():
    id=int(input("Enter students rollNumbers :"))
    fname=input("Enter students FirstName  :")
    lname=input("Enter students LastName :")
    age=int(input("Enter students Age :"))
    dob=int(input("Enter students DOB :"))
    
# create a function for view students
def view_student():
    statements
    
# create a function for delete students
def delete_student():
    statements
    
# create a function for update students
def update_student():
    statements
    
# informations ..............
print("""
============select your choice============
select 1 for Add student information
select 2 for View students information
select 3 for Delete students information
select 4 for Update students information
select 5 for Exit      
      """)

while True:
    choice=int(input('Enter your choice :'))
    if choice==1:
        add_student()
    elif choice==2:
        view_student()
    elif choice==3:
        view_student()
    elif choice==4:
        view_student()
    else: 
        print('Not selected proper given choice please select it as Given')
        break
