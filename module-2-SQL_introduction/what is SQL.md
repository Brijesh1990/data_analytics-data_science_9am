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


- ALTER: Used to modify the structure of an existing database object (e.g., adding a column to a table).

- DROP: Used to delete an existing database object (e.g., dropping a table).
- RENAME: Used to change the name of an existing database object (e.g., renaming a table).
- TRUNCATE: Used to delete all records from a table while keeping the structure intact.



2. DML (Data Manipulation Language): These commands are used to manipulate the data within a database, including inserting, updating, and deleting records. Examples include INSERT, UPDATE, and DELETE.
3. DQL (Data Query Language): These commands are used to retrieve data from a database. Examples include SELECT.
4. TCL (Transaction Control Language): These commands are used to manage transactions within a database, including committing and rolling back changes. Examples include COMMIT and ROLLBACK.



# what is database ?
1. A database is an organized collection of data that is stored and accessed electronically.

2. It is designed to efficiently store, manage, and retrieve data for various applications and purposes.

3. Databases can be classified into different types, such as relational databases, NoSQL databases, and object-oriented databases, based on their structure and data model.

   **list of database types:**
   - Relational databases: These databases organize data into tables with rows and columns, and they
    
        use SQL for data manipulation and querying. Examples include MySQL, PostgreSQL, and Oracle.


# name of all databases

1. MySQL
2. PostgreSQL
3. Oracle
4. Microsoft SQL Server
5. MongoDB
6. Cassandra
7. Redis