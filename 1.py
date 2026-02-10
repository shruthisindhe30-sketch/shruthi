use shruthi;

create table candidate(
id int primary key,
name varchar(45),
age int,
email varchar(45)
);

insert into candidate values(3, "maxi",20,"maxi12@gmail.com");
insert into candidate values(5, "mini",15,"mini34@gmail.com");
insert into candidate values(1, "mega",18,"mega56@gmail.com");

select * from candidate;
