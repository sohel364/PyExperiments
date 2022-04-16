#Diffrent joining sample queires on the HR SCHEMA
select *
from countries
left join regions
on countries.REGION_ID = regions.REGION_ID

select departments.DEPARTMENT_ID, employees.FIRST_NAME, employees.LAST_NAME
from departments
right join employees 
on departments.DEPARTMENT_ID = employees.DEPARTMENT_ID

select employees.FIRST_NAME, employees.LAST_NAME, departments.DEPARTMENT_NAME
from departments
inner join employees
on departments.DEPARTMENT_ID = employees.DEPARTMENT_ID

select departments.DEPARTMENT_NAME, employees.DEPARTMENT_ID
from departments
cross join employees
where departments.DEPARTMENT_ID = employees.DEPARTMENT_ID

select empT1.EMPLOYEE_ID, empT2.FIRST_NAME, empT1.SALARY
from employees empT1, employees empT2
where empT1.SALARY < empT2.SALARY



select employees.FIRST_NAME, employees.SALARY
from employees where SALARY > (select avg(SALARY) from employees)
order by SALARY desc
