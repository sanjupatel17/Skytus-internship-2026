use company_db ;

create table  Employee (
    EmpID INT primary key ,
    EmpName varchar(50),
    Salary INT,
    HireDate DATE
);


insert into  Employee values
(1, 'Amit', 50000, '2025-09-01'),
(2, 'Rahul', 60000, '2025-11-15'),
(3, 'Neha', 60000, '2025-12-01'),
(4, 'Priya', 45000, '2024-06-10'),
(5, 'Sanjay', 70000, '2025-10-05'),
(6, 'Rohit', 50000, '2023-03-20');

select * from Employee ;


--Find Nth Highest Salary
select max(salary) as nth_highest from Employee where salary <(select max(salary) from Employee);



alter  table Employee
add Email varchar(255);

alter table Employee drop column Email;
select * from Employee ;




create table  Users (
    UserID INT,
    Email varchar(100)
);

insert into Users values
(1, 'a@gmail.com'),
(2, 'b@gmail.com'),
(3, 'a@gmail.com'),
(4, 'c@gmail.com'),
(5, 'b@gmail.com');


--Remove Duplicate Records
with  CTE as  (
    select  *,
           row_number() OVER (
               partition by email
               order  by UserId
           ) AS rn
    from  Users
)
delete from CTE
where rn > 1;
select * from Users ;

--Find Records Common in Two Tables


select EmpId from Employee 
intersect 
select UserId from Users;


--Find Employees Hired in Last 6 Months

select EmpName from Employee 
Where  HireDate >= dateadd(month , -6, getdate());

--Find Continuous Duplicate Values


create table  Logs (
    id INT primary key,
    value varchar(10)
);

insert into Logs (id, value) values 
(1, 'A'),
(2, 'A'),
(3, 'A'),
(4, 'B'),
(5, 'B'),
(6, 'C'),
(7, 'A'),
(8, 'A');

select distinct value 
from (
select  value,
LAG(value) over (order by id) as pre_value from Logs)t
where value = pre_value;

