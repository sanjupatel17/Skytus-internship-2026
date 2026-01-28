 --Project: E-Commerce Database

create database Ecommerce ;
use Ecommerce ;

create table Customers (
    customer_id INT primary key,
    name varchar(50) NOT NULL,
    city varchar(50)
);

create table products (
    product_id INT primary key,
    product_name varchar(100) NOT NULL,
    price decimal(10,2) NOT NULL
);

create table Orders (
    order_id INT primary key,
    customer_id INT  foreign key references Customers(customer_id),
    order_date datetime default getdate(),
    amount decimal(10,2)
);

create table Order_Items (
    order_id INT  foreign key references   Orders(order_id),
    product_id INT  foreign key references  Products(product_id),
    quantity INT NOT NULL,
    primary key  (order_id, product_id)
);



insert into Customers values (1,'sanjay','Valsad'),
(2, 'Rahul', 'Delhi'),
(3, 'Anita', 'Pune'),
(4, 'Rohit', 'Bangalore'),
(5, 'Neha', 'Mumbai');


insert into Products  VALUES
(101, 'Laptop', 60000),
(102, 'Mobile', 30000),
(103, 'Headphones', 3000),
(104, 'Keyboard', 2000);

insert into Orders values
(1001, 1, '2025-01-10', 90000),
(1002, 2, '2025-01-15', 30000),
(1003, 1, '2025-02-05', 60000),
(1004, 3, '2025-02-20', 5000),
(1005, 5, '2025-03-10', 62000);

insert into Order_Items values 
(1001, 101, 1),
(1001, 102, 1),
(1002, 102, 1),
(1003, 101, 1),
(1004, 103, 1),
(1005, 101, 1),
(1005, 104, 1);

select * from Customers ;
select * from products;
select * from Orders ;
select * from Order_Items ;




-- Tasks

--Total orders per customer

select c.customer_id,c.name,
count(o.order_id) as total_orders 
from Customers c 
left join  Orders o on c.customer_id=o.customer_id 
group by c.customer_id,c.name ;

--Customers who never placed an order

select c.customer_id,c.name from Customers c 
left join  Orders o on c.customer_id=o.customer_id 
where o.order_id is null ;

--Highest selling product
select p.product_name,sum(OI.quantity) as total_quantity
from Order_Items OI
join products p on 
 oi.product_id = p.product_id
group by  p.product_name
order by  total_quantity desc;


--Monthly sales report

select  
    format(order_date, 'yyyy-MM-dd') as  Month,
    sum(amount) AS total_sales
from Orders
group by format(order_date, 'yyyy-MM-dd')
order by Month;


-- Customers with total purchase > ₹50,000

select c.customer_id,c.name, sum(o.amount) as total_purchase
from Customers c 
join Orders o
on c.customer_id=o.customer_id
group by c.customer_id,c.name 
having sum(o.amount)>50000 ;

--Top 3 cities by revenue

select top 3
    c.city,
    sum(o.amount) as total_revenue
from Customers c
JOIN Orders o
on c.customer_id = o.customer_id
group by c.city
order by total_revenue desc;





 --   assignmet 8  Tasks

--Add index to improve search on orders.
Create index  idx_orders_customer_id
on Orders(customer_id);


--Use EXPLAIN to analyze query
set statistics profile on ;

select *
from Orders
where customer_id = 1;

set statistics profile off ;


--Optimize a slow join query
select  *
from Customers c
JOIN Orders o
on  c.customer_id = o.customer_id;

Create index  idx_orders_customer_id
on Orders(customer_id);

select  
    c.name,
    o.amount
from Customers c
JOIN Orders o
on  c.customer_id = o.customer_id;


--Explain when index should not be used

--Returns almost all rows 

SELECT * FROM orders WHERE amount > 5000;



SELECT * 
FROM Orders
WHERE Order_id = 1003;
