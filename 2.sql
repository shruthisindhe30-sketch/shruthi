use shruthi;

create table employees(
emp_id int primary key,
name varchar(45) not null,
dept_id int,
manager_id int 
);

create table departments(
dept_id int,
dept_name varchar(45) not null
);

insert into employees values(1,"Alice",10,null);
insert into employees values(2,"Bob",20,1);
insert into employees values(3,"Charlie",null,1);

insert into departments values(10,"HR");
insert into departments values(20,"IT");
insert into departments values(30,"Finance");

select * from employees;      
select * from departments;

SELECT e.name, d.dept_name
FROM Employees e
INNER JOIN Departments d
ON e.dept_id = d.dept_id;

SELECT e.name, d.dept_name
FROM Employees e
LEFT JOIN Departments d
ON e.dept_id = d.dept_id;

SELECT e.name, d.dept_name
FROM Employees e
RIGHT JOIN Departments d
ON e.dept_id = d.dept_id;

SELECT e.name, d.dept_name
FROM Employees e
CROSS JOIN Departments d;

SELECT e.name AS employee,
       m.name AS manager
FROM Employees e
LEFT JOIN Employees m
ON e.manager_id = m.emp_id;





