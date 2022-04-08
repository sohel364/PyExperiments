create table if not exists departments(
	id int primary key auto_increment,
    name varchar(30),
    head varchar(30),
    no_of_faculties int
);

create table if not exists students(
	id int primary key auto_increment,
    name varchar(30),
    dob date,
    admission_date date,
    cgpa float(3,2),
    dept int,    
    constraint fk_students_departments foreign key(dept)
    references departments(id) on delete cascade
);

#Create table or table column name with space : Using ``
# name with space
create table `teachers and students` (  
	id int(10),
    name varchar(50),
    `date of birth` date)
# name with space
CREATE TABLE table_name (
 id int(10),
 name VARCHAR(50),
 `date of birth` DATE,
 `joining date` DATE
);


###### alter table with foreign key constraint #######
alter table students
	add constraint fk_student_department foreign key(dept) references departments(id)
    on delete restrict
    ## Thie fk_student_department restricts users from removing department while there is use of department id in relational tables


## alter constraint
alter table students  
add constraint fk_students_departments foreign key(dept)
    references departments(id) on delete cascade
    
## drop constraint
alter table students
drop constraint fk_student_department

## updateing a constraing requires dropping it first and then adding the expected constraint newly

#ALTER TABLE 
alter table students
	change column oldColumnName newColumnName date

#count rows 
select count(*) from employees
# Example : Select distinct first name count from employee table 
select count(distinct employees.FIRST_NAME) from employees  

# Example : select employees ording by hired date
select FIRST_NAME, HIRE_DATE from employees order by employees.HIRE_DATE desc




























