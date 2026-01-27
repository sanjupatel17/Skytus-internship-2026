 
 
 
create database BANK;
use BANK;
 




 CREATE TABLE Accounts (
    AccountId INT PRIMARY KEY,
    AccountHolder VARCHAR(50),
    Balance DECIMAL(10,2)
);

INSERT INTO Accounts (AccountId, AccountHolder, Balance)
VALUES
(1, 'Sanjay', 5000.00),
(2, 'Rahul', 3000.00);

SELECT * FROM Accounts;

 --Tasks



--Start a transaction

--Insert record into accounts

--Rollback changes

BEGIN TRANSACTION;

INSERT INTO Accounts (AccountId, AccountHolder, Balance)
VALUES (3, 'Anita', 4000.00);

-- Something went wrong → rollback
ROLLBACK;

SELECT * FROM Accounts;


--Commit valid transactions

BEGIN TRANSACTION;

INSERT INTO Accounts (AccountId, AccountHolder, Balance)
VALUES (3, 'Anita', 4000.00);

COMMIT;

SELECT * FROM Accounts;



--Demonstrate transfer of money using transaction

BEGIN TRANSACTION;


update Accounts set Balance = Balance - 1000 
where AccountId = 1 ;

UPDATE Accounts
SET Balance = Balance + 1000
WHERE AccountId = 2;


commit ;

