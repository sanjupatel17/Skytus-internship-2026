use Studentdb ;

create table students (student_id INT ,name VARCHAR(50),department VARCHAR(50), year INT, marks INT )



insert into students values(1,'sanju','IT',4,90);
insert into students values(2,'Nij','CO',4,98);
insert into students values(3,'Parth','EL',3,96);
insert into students values(4,'Het','CO',2,60);
insert into students values(5,'Henil','CSE',1,94);
insert into students values(6,'Meet','CSE',4,91);



--Display all student records

SELECT * FROM students ;

--Display only name and department
select name,department from students ;

--Find students with marks greater than 75

select name,marks from students  where marks>75;

--Display students from CSE department


select name,department from students where department='CSE';

--Sort students by marks (descending)
select name,marks from students order by marks DESC ;

--Display top 3 scorers"

SELECT top 3 name, marks
FROM students
ORDER BY marks DESC;

