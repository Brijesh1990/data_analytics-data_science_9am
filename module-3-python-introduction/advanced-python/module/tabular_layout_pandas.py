# install pandas (pip install pandas)
# pandas is used to create a dataset in tabular layout

# employee={
    
#     "name":["nimavat","aryan","misri","brijesh"],
#     "age":[27,19,19,35]
# }

# print(employee)


# create an tabular layout using data frame
# install pandas pip install pandas
# pip show pandas

import pandas as pd
employee={
    
    "firstname":["aryan","giriraj","mishri","brijesh","karan"],
    
    "lastname":["harkhani","nimavat","jasani","pandey","rathod"]
}

# create a dataframe using pandas
print(pd.DataFrame(employee))
# DataFrame() create an tabular layout of employee
