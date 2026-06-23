import pandas as pd
employee={
    
    "firstname":["aryan","giriraj","mishri","brijesh","karan"],
    "lastname":["harkhani","nimavat","jasani","pandey","rathod"],
    "age":[20,27,20,35,28],
    "salary":[15500,35800,15800,11500,15900],
    "department":["IT","HR","CSE","IT","marketing"]
}

# create a dataframe using pandas
# print(pd.DataFrame(employee))
# DataFrame() create an tabular layout of employee
# find sum of salary of all employee
df=pd.DataFrame(employee);
print(df)
# sum salary
print("########  sum of all employee salary##########")
sum_salary=df["salary"].sum();
print("Sum of salary of employee :",sum_salary)

# max salary
print("######## max salary of  employee ##########")
max_salary=df["salary"].max();
print("Max of salary of employee :",max_salary)

# min salary
print("######## min salary of  employee ##########")
min_salary=df["salary"].min();
print("Min of salary of employee :",min_salary)

# avg salary
print("######## average salary of  employee ##########")
avg_salary=df["salary"].median();
print("Median of salary of employee :",avg_salary)