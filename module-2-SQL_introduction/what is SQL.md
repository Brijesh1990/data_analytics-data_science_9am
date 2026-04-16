# what is SQL ?
1. SQL stands for Structured Query Language. 
2. It is a programming language used to manage and manipulate relational databases.
3. SQL allows users to create, read, update, and delete data in a database.
4. It is widely used in various applications, including web development, data analysis, and database management.
5. SQL is known for its simplicity and efficiency in handling large amounts of data, making it an essential tool for developers and data professionals.
6. SQL is case-insensitive, meaning that keywords can be written in uppercase or lowercase letters without affecting the functionality of the code.
7. Some common SQL commands include SELECT, INSERT, UPDATE, DELETE, CREATE, and DROP.
8. SQL is used to interact with databases such as MySQL, PostgreSQL, Oracle, and Microsoft SQL Server.
9. SQL is a standard language for relational database management systems (RDBMS) and is supported by most database systems, making it a versatile and widely adopted language in the field of data management.
10. SQL allows users to perform complex queries and operations on databases, such as filtering, sorting, and joining tables, making it a powerful tool for data analysis and reporting.
11. SQL is also used for database administration tasks, such as creating and managing database schemas, setting permissions, and optimizing database performance.
12. SQL is a declarative language, meaning that users specify what they want to achieve rather than how to achieve it, allowing for more efficient and optimized query execution by the database engine.
13. SQL is an essential skill for data analysts, data scientists, and database administrators, as it enables them to effectively manage and analyze data stored in relational databases, making it a valuable tool for making informed business decisions and gaining insights from data.


# advantages of SQL
1. SQL is a powerful and efficient language for managing and manipulating relational databases, allowing users to perform complex queries and operations on large amounts of data.

2. SQL is widely supported by various database systems, making it a versatile and widely adopted language in the field of data management.

3. SQL is a declarative language, allowing users to specify what they want to achieve rather than how to achieve it, which can lead to more efficient and optimized query execution by the database engine.

4. SQL provides a standardized way to interact with databases, making it easier for developers and data professionals to work with different database systems without needing to learn new languages or syntax.

5. SQL allows for easy data manipulation and retrieval, enabling users to quickly access and analyze data stored in relational databases, which can lead to faster decision-making and improved business outcomes.

6. SQL supports data integrity and security features, such as constraints, transactions, and user permissions, which help ensure the accuracy and confidentiality of data stored in databases.

7. SQL is a widely used language in various industries, including finance, healthcare, e-commerce, and technology, making it a valuable skill for professionals in these fields to have in order to effectively manage and analyze data.

8. SQL allows for easy integration with other programming languages and tools, making it a flexible and powerful tool for data analysis, reporting, and application development.

9. SQL provides a rich set of functions and operators for performing calculations, aggregations, and data transformations, allowing users to derive insights and perform complex data analysis tasks on their databases.

10. SQL is a mature and well-established language with a large community of users and developers, which means that there are plenty of resources, documentation, and support available for learning and using SQL effectively.


# types of database

1. MySQL
2. PostgreSQL
3. Oracle
4. Microsoft SQL Server
5. MongoDB
6. Cassandra
7. Redis


# SQL commands

**types of SQL commands:**

1. DDL (Data Definition Language): These commands are used to define and manage the structure of a database, including creating, altering, and dropping tables and other database objects. Examples include CREATE, ALTER, and DROP , RENAME , TRUNCATE.

**list of query or commands in DDL:**
- CREATE: Used to create a new database or database object (e.g., database, table, view, index).

```
create database databasename;
or 
create database flip_cart;

```

# rules to create database

1. The database name must be unique within the database server.
2. The database name must start with a letter (a-z) or an underscore (_).
3. The database name can contain letters, numbers, and underscores, but it cannot contain spaces or special characters.


-CREATE table : create table structures using create commands
**syntax to create table:**

```
create table tablename(
column1 datatype,
column2 datatype,
column3 datatype,
...
);

```
**examples to create table:**
```
create table employee(
id int,
name varchar(50),
age int,
department varchar(50)
);

```

**data types and size of column in tables**
1. int (integer): Used to store integer values (e.g., 1, 100, -50) default size 11 first column as a id auto_increment primary key.

2. varchar(size): Used to store variable-length character strings, where size specifies the maximum number of characters (e.g., varchar(50) can store up to 50 characters). default size 255

3. date: Used to store date values in the format 'YYYY-MM-DD' (e.g., '2024-06-01').

4. float: Used to store floating-point numbers (e.g., 3.14, price : 25.50) .

5. boolean: Used to store true/false values (e.g., true, false).

6. text: Used to store large amounts of text data (e.g., articles, descriptions).

7. datetime: Used to store date and time values in the format 'YYYY-MM-DD HH:MM:SS' (e.g., '2024-06-01 12:30:00').

8. char(size): Used to store fixed-length character strings, where size specifies the exact number of characters (e.g., char(10) can store exactly 10 characters).

9. decimal(size, d): Used to store decimal numbers with a specified precision (size) and scale (d) (e.g., decimal(10, 2) can store numbers with up to 10 digits and 2 decimal places).

10. enum (enumerated): Used to store a predefined set of values (e.g., enum('small', 'medium', 'large') can store only the values 'small', 'medium', or 'large').

examples: status enum('active', 'inactive') can store only the values 'active' or 'inactive'.

11. bigint: Used to store large integer values (e.g., 1234567890123456789) default size 20

12. auto_increment: Used to automatically generate a unique value for a column (e.g., id int auto_increment) often used for primary key columns.


# rules to create table

1. The table name must be unique within the database.
2. The table name must start with a letter (a-z) or an underscore (_).
3. The table name can contain letters, numbers, and underscores, but it cannot contain spaces or special characters. (@ , $ , % , & , * , etc.)
4. Each column in the table must have a unique name and a specified data type (e.g., int, varchar, date).
5. The table must have at least one column defined, and it can have a maximum of 1024 columns, depending on the database system being used.


**create a table of contactus:**
```
create table contactus(
id int auto_increment primary key,
name varchar(100),
email varchar(100),
phone bigint,
message text,
created_at datetime
);

```

**create table of country:**
```   
create table country(
id int auto_increment primary key,
name varchar(100),
population bigint,
area float,
capital varchar(100)
);

```

**home work:**

1. create student tables
2. create employee tables
3. create product tables
4. create order tables
5. create customer tables
6. create supplier tables
7. create department tables
8. create city tables
9. create country tables
10. create state tables


# ALTER: 

1. Used to modify the structure of an existing database tables (e.g., adding a column to a table).
2. alter is used to add , modify , update a new column in existing tables 

**alter query**

1. how to add new column after pid in a table
```
alter table products add productimage varchar(255) after pid;
```

2. how to add new column at last 

```
alter table department add added_date datetime;
```  

3. how to change a columnname in a table

```
alter table department change departmentname depname varchar(255);

```    
# RENAME: 

1. Used to change the name of an existing database table (e.g., renaming a table).
2. Rename is used to change the tablename

**how to change tablename**
```
rename table customer to shop_consumers;

```

# DROP: Used to delete an existing database object (e.g., dropping a table).

1. Drop is used to delete database and table structured permanently
2. drop is deleted tables structured and data permanently

**how to drop table**
```
drop table employee;
```
**how to drop database**
```
drop database dbshop;
```

# note:after drop we can not be rollback the data and structure of database and tables

# TRUNCATE: Used to delete all records from a table while keeping the structure intact.

1. Truncate is used to delete all records or rows from table.
2. Truncate is empty the table records but the structure of table is not deleted.
**how to truncate table**
```
truncate table employee;
or
truncate table shop_country;
```
# note : after truncate we can not be rollback the data but the structure of table is not deleted


**Home work:**

1. Create a table named "students" with columns for id, name, age, and grade.
2. Alter the "students" table to add a new column for email.
3. Rename the "students" table to "school_students".
4. Drop the "school_students" table.
5. Create a table named "employees" with columns for id, name, department, and salary.
6. Alter the "employees" table to add a new column for hire_date.
7. Rename the "employees" table to "company_employees".
8. Drop the "company_employees" table.
9. Create a table named "products" with columns for id, name, price, and quantity.
10. Alter the "products" table to add a new column for description.
11. Rename the "products" table to "store_products".
12. Drop the "store_products" table.
13. Create a table named "orders" with columns for id, customer_name, product_name, and order_date.
14. Alter the "orders" table to add a new column for order_status.
15. Rename the "orders" table to "customer_orders".
16. Drop the "customer_orders" table.
17. Create a table named "customers" with columns for id, name, email, and phone.
18. Alter the "customers" table to add a new column for address.
19. Rename the "customers" table to "client_customers".
20. Drop the "client_customers" table.


# DML (Data Manipulation Language): These commands are used to manipulate the data within a # name of all databases

1. DML stands for Data Manipulation Language.
2. DML commands are used to insert data into tables, deleted data from tables , update data from tables.
1. insert : used to insert data into tables
**how to insert single record in a table**
```
insert into students (id, name, age, grade) values (1, 'John Doe', 20, 'A');
```
**how to insert multiple record in a table**
```
insert into students (id, name, age, grade) values 
(2, 'Jane Smith', 22, 'B'),
(3, 'Michael Johnson', 19, 'A'),
(4, 'Emily Davis', 21, 'C');

or

insert into shop_state(sname,added_date) values
('uttar pradesh','07/04/2026'),
('mahrastra','07/04/2026'),
('madhya pradesh','07/04/2026');

```

2. delete : used to delete data from tables single data delete or all table data delete and particular column data delete.

```
1. delete all data from table 
delete from shop_state;

2. delete from shop_state where sid=3;

3. delete from shop_state where sid in(1,3);

4. delete from shop_state where sid between 50 and 1000;    


```

3. update : used to update data from tables

```
update shop_state set sname='rajsthan' where sid=4;
or
update shop_state set sname='rajsthan', added_date='09/04/2026' where sid=4;
or
update shop_contactus set name='aryan',email='aryan007@gmail.com',phone=6534587898,comment='hey i am atyan' where id=1;
```

**note:after delete we rollback data using TCL**


3. DQL :DQL stands for data query language

1. DQL select data 
2. DQL fetch data from tables 
3. DQL select all data from table , particular data from tables etc.


**DQL commands**

```
1. select * from shop_state;
2. select * from shop_state where sid=2;
3. select * from shop_state where sname='rajsthan';
4. select * from shop_state where sid in (1,3,5,7);
5. select * from shop_state where sid between 51 and 1000;
6. select * from shop_state where sid between 4 and 9;
7. select * from shop_state where sid limit 0,5;
8. select * from shop_state where sid limit 2,5;
```     

**order by:order by filter data from tables in ascending or descending order**

1. order by ascending or descending order:

```
1. select * from shop_state order by sname; 
2. select * from shop_state order by sname asc;
3. select * from shop_state order by sid desc;
4. select * from shop_state order by sid asc; 

``` 

**group by : group by filter data in group of columns**

2. group by :select and filter data from tables on group of columns 

```
find the sum of salary on different-2 departments from shop_employee

1. select sum(salary),department from shop_employees GROUP by department;

```   

**like operator : like operator is used to search data from tables using first and last or all character match in any word or name and its denoted by %**

```
1. select * from shop_state where sname like 'B%';
2. select * from shop_state where sname like 'A%';
3. select * from shop_state where sname like 'B%' ORDER by sname asc;
4. select * from shop_state where sname like '%l' ORDER by sname asc;
5. select * from shop_state where sname like '%e' ORDER by sname asc;
6. select * from shop_state where sname like '%a%' ORDER by sname asc;
7. select * from shop_state where sname like '%a%' ORDER by sid desc;

```
# sql function : sql function are provide some inbuilt function of sql

**types of SQL function**

# aggrigate function 

1. sum() : sum is used to sum the salary of employee
     
     examples :select sum(salary) from shop_employees; 
               or
               select sum(salary) as sum_of_salary from shop_employees;
                
2. avg() : find average of salary 
           
         examples: select avg(salary) as average_salary from shop_employees;
                   or
                   select avg(salary)  from shop_employees;  
          
3. max(): find the maximum values from table or salary of employee
       
       examples : select max(salary) from shop_employees;
                  or
                  select max(salary) as max_salary_employee from shop_employees;


4. min() : find the minimum values from tables or salary of employee
          
          examples : select min(salary) from shop_employees;
                     or 
                     select min(salary) as minimum_salary_employee from shop_employees;

5. count() : count the total numbers of employee
           
           examples : select count(id) as total_numbers_employee from shop_employees;
                      or
                      select count(id)  from shop_employees; 

#  scalar function

1. first() : select a first rows from tables 
          examples: select first from shop_employees;

2. last() : select last rows from tables 
           examples : select last from shop_employees;  
3. lcase() : select and convert any column in lower case 
           examples : select lcase(name) from shop_employees
4. ucase() : select and convert any column in upper case 
           examples : select ucase(name) from shop_employees 


# subquery : query within another query i.e called subquery 

    examples : query within another query i.e called subquery find the second highest salary from shop_employees

**second highest salary**

```
select max(salary) from shop_employees where salary <(select max(salary) from shop_employees);
or
select max(salary) as second_highest_salary from shop_employees where salary <(select max(salary) from shop_employees);

```

# whats is alias in SQL 

  1. alias is used to convert any column name in tables 

  ```
  select name as firstname from shop_employees

  ```  

# SQL key constraints 

  1. key constraints provides limit on tables 
  2. key constraints used to set limitation on tables 
  3. key constraints set relationship between tables 
  4. key constraints set to normalized tables 

# types of key constraints 

  1. primary key
  2. foreign key
  3. unique key 
  4. compound key

# primary key (pk) : 

  1. A primary key set on id 
  2. A pk is always set only once time in a tables 
  3. A pk is always auto_increments 
  4. A pk is never return null values and stored a unique values 


| id | employee_name | age | salary |
|----|---------------|-----|--------|
| 1  | Amit Shah     | 65  | 100000 |
| 2  | Neha Patel    | 22  | 25000  |
| 3  | Raj Mehta     | 25  | 28500  |
| 4  | Priya Desai   | 24  | 29500  |  
| 5  | Karan Singh   | 25  | 30500  |

# note : id is always primary key with auto_increments 

 **create in SQL**

 ```
 CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(100)
);

 ```
# unique key (uk) : 

  1. A unique key set on any columns
  2. A uk is always set to create a unique columns does not stored dublicate values 
  3. A uk is provides uniquely stored data
  4. A uk is  return once time a null values 


| id | employee_name | age | salary |email |  phone        |
|----|---------------|-----|--------|------|---------------|
| 1  | Amit Shah     | 65  | 100000 |a@gmail.com|9998003879|
| 2  | Neha Patel    | 22  | 25000  |n@gmail.com|9998003578|
| 3  | Raj Mehta     | 25  | 28500  |r@gmail.com|9173357217|
| 4  | Priya Desai   | 24  | 29500  |p@gmail.com|653548568 |  
| 5  | Karan Singh   | 25  | 30500  |k@gmail.com|631515151 |

# note : UK provides to does not stored a dublicate values in tables

 **create in SQL a unique key**
 ```
 ALTER TABLE `employees` ADD UNIQUE(`phone`);
 or
 ALTER TABLE `employees` ADD UNIQUE(`email`);

 ``` 


# foreign key (fk) : 

  1. A fk key set on any columns create a relationship
  2. A fk create a relationship between one table to another table with common field
  3. A fk is dublicate and provides relationship


**country**

|cid     |name      |
|--------|----------|
| 1      |India     |
| 2      |USA       |

**users**

| uid |    name      | age | salary |email |  phone        |  cid  |
|----|---------------|-----|--------|------|---------------|-------|
| 1  | Amit Shah     | 65  | 100000 |a@gmail.com|9998003879|   1   |
| 2  | Neha Patel    | 22  | 25000  |n@gmail.com|9998003578|   2   | 
| 3  | Raj Mehta     | 25  | 28500  |r@gmail.com|9173357217|   1   |
| 4  | Priya Desai   | 24  | 29500  |p@gmail.com|653548568 |   2   |
| 5  | Karan Singh   | 25  | 30500  |k@gmail.com|631515151 |   2   |

# note : fK provides to   stored a dublicate values in tables for relationship

 **create in SQL a fk key**

```
 create table country
(
cid int AUTO_INCREMENT primary key,
cname varchar(255)    
) 
```

```
 create table users
(
uid int AUTO_INCREMENT primary key,
name varchar(255),
email varchar(255),
phone bigint,
cid int REFERENCES country(cid)    
) 
 ``` 

```
create table products
(
pid int AUTO_INCREMENT primary key,
catid int REFERENCES categories(catid),    
subcatid int REFERENCES subcategories(subcatid),    
pname varchar(255),
qty int,
price int,
descriptions text    
)

```
