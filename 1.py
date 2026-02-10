use shruthi;

create table user(
id int primary key,
name varchar(45),
age int,
email varchar(45)
);

insert into user values(3, "maxi",20,"maxi12@gmail.com");
insert into user values(5, "mini",15,"mini34@gmail.com");
insert into user values(1, "mega",18,"mega56@gmail.com");

select * from user;

UPDATE user
SET email = 'alice@gmail.com',
    age = 27,
    name = "Alice"
WHERE id = 3;

DELETE FROM user
WHERE id = 1;


