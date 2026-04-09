# statements to create a contact tables 

  1. create a database command

     ```
         create database dbshop;
      ```

  2. create contact table commands 

     ```
      create table contact
(
 contactid int AUTO_INCREMENT primary key,
 employeeid int,
 firstname varchar(255),
 lastname varchar(255),
 city varchar(255),
 state varchar(255),
 zip int,
 email varchar(255),
 ismain boolean,
 phone bigint   

)

     ```



3.      