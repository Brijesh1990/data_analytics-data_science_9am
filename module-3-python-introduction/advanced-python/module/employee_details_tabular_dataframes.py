import pandas as pd
employee={
    
    "firstname":["aryan","giriraj","mishri","brijesh","karan"],
    "lastname":["harkhani","nimavat","jasani","pandey","rathod"],
    "age":[20,27,20,35,28],
    "salary":[15500,35800,15800,11500,15900],
    "department":["IT","HR","CSE","IT","marketing"]
}

# create a dataframe using pandas
print(pd.DataFrame(employee))
# DataFrame() create an tabular layout of employee
