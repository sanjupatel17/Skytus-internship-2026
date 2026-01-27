create database company_db;

use company_db;

create table employees(emp_id INT,emp_name varchar(50),dept_id INT,salary INT);

create table departments(department_id INT,dept_name varchar(50));



select * from employees;
select * FROM departments ;

INSERT INTO departments (department_id, dept_name)
VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance'),
(4, 'Sales');

INSERT INTO employees (emp_id, emp_name, dept_id, salary)
VALUES
(101, 'Sanju', 1, 50000),
(102, 'Nij', 2, 45000),
(103, 'Parth', 3, 60000),
(104, 'Het', 1, 55000),
(105, 'Henil', 4, 40000),
(106, 'Meet', 3, 65000);


-- Tasks

-- Display employee name with department name

select e.emp_name,d.dept_name 
from departments d right join  employees e  on d.department_id=e.dept_id ;


--Display employees earning more than 50,000

select emp_name from employees where salary >50000 ;

--Display department-wise total salary

select d.dept_name,SUM(e.salary) as toatal_salary  
from departments d right join employees e on d.department_id = e.dept_id 
group by dept_name;


--Display departments with more than 2 employees
SELECT 
    e.emp_id,
    e.emp_name,
    d.dept_name,
    e.salary
FROM employees e
JOIN departments d
ON e.dept_id = d.department_id;


--Display employees without a department


select * from departments where department_id is null ;

