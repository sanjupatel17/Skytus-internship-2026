use comapny_db ;

-- Users table
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    email VARCHAR(50),
    password VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT GETDATE()
);

SELECT * FROM Users;


-- Orders table
CREATE TABLE Orders (
    OrderId INT PRIMARY KEY,
    user_id INT,
    OrderDate DATETIME DEFAULT GETDATE(),
    Amount DECIMAL(10,2),

    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

SELECT * FROM Orders;

INSERT INTO Users (user_id, email, password, created_at)
VALUES
(1, 'sanjay@gmail.com', 'pass@123', '2026-01-20 10:15:00'),
(2, 'rahul@gmail.com', 'rahul@456', '2026-01-21 11:30:00'),
(3, 'anita@gmail.com', 'anita@789', '2026-01-22 09:45:00');


INSERT INTO Orders (OrderId, user_id, OrderDate, Amount)
VALUES
(105, 1, '2026-01-25 14:30:00', 1800.00),
(106, 2, '2026-01-26 16:45:00', 4200.25);




--Create index on email column
create index idx_emial on Users(email);


--Create view to display user order summary

CREATE VIEW vw_UserOrders
AS
SELECT
    u.user_id,
    u.email,
    u.created_at AS UserCreatedDate,
    o.OrderId,
    o.Amount,
    o.OrderDate
FROM Users u
JOIN Orders o
ON u.user_id = o.user_id;


select * from vw_UserOrders ;