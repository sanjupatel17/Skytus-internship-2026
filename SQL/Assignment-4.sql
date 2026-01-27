select * from employees ;
select * from departments ;

 -- Tasks

--Find employees earning more than average salary

select emp_name, salary
from employees
where salary > (
    select  AVG(salary)
    from employees );


-- Find department with highest total salary
select d.dept_name, SUM(e.salary) as total_salary
from departments d
join employees e
    on e.dept_id = d.department_id
 group by  d.dept_name
having SUM(e.salary) = (
    select MAX(total_sal)
    from (
        select  SUM(salary) AS total_sal
        from  employees
        group by dept_id
    ) t
);



--Display employee with second highest salary

select  emp_name, salary AS second_highest_salary
from employees
where salary = (
    select  MAX(salary)
    from employees
    where  salary < (
        select MAX(salary)
        from employees
    )
);

--display employees working in same department as "sanju" ;

Select emp_name
from employees
where dept_id = (
    select dept_id
    from employees
    where  emp_name = 'sanju'
);
