--Tasks 1: Database Design: 
--1. Create the database named "HMBank"
--2. Define the schema for the Customers, Accounts, and Transactions tables based on the 
--provided schema.
--4. Create an ERD (Entity Relationship Diagram) for the database.
--5. Create appropriate Primary Key and Foreign Key constraints for referential integrity.
--6. Write SQL scripts to create the mentioned tables with appropriate data types, constraints, 
--and relationships. 
--• Customers
--• Accounts
--• Transactions

--Tasks 2: Select, Where, Between, AND, LIKE:
--1. Insert at least 10 sample records into each of the following tables. 
--• Customers
--• Accounts
--• Transactions
--2. Write SQL queries for the following tasks:
--1. Write a SQL query to retrieve the name, account type and email of all customers. 
--2. Write a SQL query to list all transaction corresponding customer.
--3. Write a SQL query to increase the balance of a specific account by a certain amount.
--4. Write a SQL query to Combine first and last names of customers as a full_name.
--5. Write a SQL query to remove accounts with a balance of zero where the account 
--type is savings.
--6. Write a SQL query to Find customers living in a specific city.
--7. Write a SQL query to Get the account balance for a specific account.
--8. Write a SQL query to List all current accounts with a balance greater than $1,000.
--9. Write a SQL query to Retrieve all transactions for a specific account.
--© Hexaware Technologies Limited. All rights www.hexaware.com
--10. Write a SQL query to Calculate the interest accrued on savings accounts based on a 
--given interest rate.
--11. Write a SQL query to Identify accounts where the balance is less than a specified 
--overdraft limit.
--12. Write a SQL query to Find customers not living in a specific city.

--Tasks 3: Aggregate functions, Having, Order By, GroupBy and Joins:
--1. Write a SQL query to Find the average account balance for all customers. 
--2. Write a SQL query to Retrieve the top 10 highest account balances.
--3. Write a SQL query to Calculate Total Deposits for All Customers in specific date.
--4. Write a SQL query to Find the Oldest and Newest Customers.
--5. Write a SQL query to Retrieve transaction details along with the account type.
--6. Write a SQL query to Get a list of customers along with their account details.
--7. Write a SQL query to Retrieve transaction details along with customer information for a 
--specific account.
--8. Write a SQL query to Identify customers who have more than one account.
--9. Write a SQL query to Calculate the difference in transaction amounts between deposits and 
--withdrawals.
--10. Write a SQL query to Calculate the average daily balance for each account over a specified 
--period.
--11. Calculate the total balance for each account type.
--12. Identify accounts with the highest number of transactions order by descending order.
--13. List customers with high aggregate account balances, along with their account types.
--14. Identify and list duplicate transactions based on transaction amount, date, and account.




CREATE DATABASE HMBank;
USE HMBank;

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    DOB DATE NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    phone_number VARCHAR(10) UNIQUE NOT NULL,
    address VARCHAR(50) NOT NULL
);

CREATE TABLE Accounts (
    account_id INT PRIMARY KEY,
    customer_id INT,
    account_type VARCHAR(20) NOT NULL,
    balance INT NOT NULL DEFAULT 0,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);


CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT,
    transaction_type VARCHAR(20) NOT NULL,
    amount INT NOT NULL,
    transaction_date DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id) ON DELETE CASCADE
);

INSERT INTO Customers (customer_id, first_name, last_name, DOB, email, phone_number, address)
VALUES
(1, 'Amit', 'Sharma', '1990-02-15', 'amit.sharma@gmail.com', '9876543210', '45, M Road, New Delhi'),
(2, 'Rohit', 'Verma', '1985-06-21', 'rohit.verma@gmail.com', '9123456789', '12, Andheri East, Mumbai'),
(3, 'Priya', 'Singh', '1992-09-10', 'priya.singh@gmail.com', '9008765432', '78, Park Street, Kolkata'),
(4, 'Kiran', 'Patel', '1988-12-05', 'kiran.patel@gmail.com', '9012345678', '22, C G Road, Ahmedabad'),
(5, 'Raj', 'Kumar', '1993-03-19', 'raj.kumar@gmail.com', '8787654321', '56, Brigade Road, Bangalore'),
(6, 'Anita', 'Rao', '1987-07-14', 'anita.rao@gmail.com', '9112345678', '17, Banjara Hills, Hyderabad'),
(7, 'Vijay', 'Desai', '1995-01-30', 'vijay.desai@gmail.com', '8987654321', '34, Race Course Road, Chennai'),
(8, 'Deepika', 'Joshi', '1991-08-08', 'deepika.joshi@gmail.com', '9871234567', '9, Marine Drive, Mumbai'),
(9, 'Suresh', 'Naik', '1989-11-22', 'suresh.naik@gmail.com', '9009876543', '28, Residency Road, Bangalore'),
(10, 'Pooja', 'Reddy', '1994-04-25', 'pooja.reddy@gmail.com', '9345678901', '15, Hitech City, Hyderabad');

INSERT INTO Accounts (account_id, customer_id, account_type, balance)
VALUES
(1, 1, 'savings', 50000),
(2, 2, 'current', 100000),
(3, 3, 'savings', 75000),
(4, 4, 'current', 120000),
(5, 5, 'savings', 65000),
(6, 6, 'zero_balance', 0),
(7, 7, 'savings', 90000),
(8, 8, 'current', 110000),
(9, 9, 'zero_balance', 0),
(10, 10, 'savings', 70000);


INSERT INTO Transactions (transaction_id, account_id, transaction_type, amount, transaction_date)
VALUES
(1, 1, 'deposit', 2000, '2024-09-20'),
(2, 2, 'withdrawal', 5000, '2024-09-22'),
(3, 3, 'deposit', 3000, '2024-09-21'),
(4, 4, 'transfer', 7000, '2024-09-23'),
(5, 5, 'withdrawal', 1500, '2024-09-24'),
(6, 6, 'deposit', 10000, '2024-09-25'),
(7, 7, 'deposit', 5000, '2024-09-26'),
(8, 8, 'withdrawal', 2500, '2024-09-25'),
(9, 9, 'deposit', 4000, '2024-09-27'),
(10, 10, 'deposit', 3000, '2024-09-28');


SELECT c.first_name, c.last_name, c.email, a.account_type
FROM Customers c
INNER JOIN Accounts a ON c.customer_id = a.customer_id;

SELECT c.first_name, c.last_name, t.transaction_type, t.amount, t.transaction_date
FROM Customers c
INNER JOIN Accounts a ON c.customer_id = a.customer_id
INNER JOIN Transactions t ON a.account_id = t.account_id;

UPDATE Accounts
SET balance = balance + 5000  
WHERE account_id = 1;  

SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM Customers;

DELETE FROM Accounts
WHERE balance = 0 AND account_type = 'savings';

SELECT first_name, last_name, address
FROM Customers
WHERE address LIKE '%Mumbai%';

SELECT balance
FROM Accounts
WHERE account_id = 1;  

SELECT customer_id, account_id, balance
FROM Accounts
WHERE account_type = 'current' AND balance > 1000;  

SELECT transaction_id, transaction_type, amount, transaction_date
FROM Transactions
WHERE account_id = 1;  


SELECT account_id, balance, balance * 0.05 AS interest_accrued  
FROM Accounts
WHERE account_type = 'savings';


SELECT account_id, balance
FROM Accounts
WHERE balance < -5000; 

SELECT first_name, last_name, address
FROM Customers
WHERE address NOT LIKE '%Delhi%';


SELECT AVG(balance) AS average_balance
FROM Accounts;


SELECT TOP 10 account_id, customer_id, balance
FROM Accounts
ORDER BY balance DESC;

SELECT SUM(amount) AS total_deposits
FROM Transactions
WHERE transaction_type = 'deposit' AND transaction_date = '2024-09-28';


SELECT TOP 1 * 
FROM Customers
ORDER BY DOB ASC;

SELECT TOP 1 * 
FROM Customers
ORDER BY DOB DESC;


SELECT t.transaction_id, t.transaction_type, t.amount, t.transaction_date, a.account_type
FROM Transactions t
JOIN Accounts a ON t.account_id = a.account_id;


SELECT c.customer_id, c.first_name, c.last_name, a.account_id, a.account_type, a.balance
FROM Customers c
JOIN Accounts a ON c.customer_id = a.customer_id;


SELECT t.transaction_id, t.transaction_type, t.amount, t.transaction_date, c.first_name, c.last_name, c.email,
c.DOB,c.address
FROM Transactions t
JOIN Accounts a ON t.account_id = a.account_id
JOIN Customers c ON a.customer_id = c.customer_id
WHERE t.account_id = 1;  


SELECT c.customer_id, c.first_name, c.last_name, COUNT(a.account_id) AS num_accounts
FROM Customers c
JOIN Accounts a ON c.customer_id = a.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING COUNT(a.account_id) > 1;



SELECT 
    a.account_id,
    ISNULL(d.total_deposits, 0) AS total_deposits,
    ISNULL(w.total_withdrawals, 0) AS total_withdrawals,
    ISNULL(d.total_deposits, 0) - ISNULL(w.total_withdrawals, 0) AS difference
FROM 
    Accounts a
LEFT JOIN 
    (SELECT account_id, SUM(amount) AS total_deposits 
     FROM Transactions 
     WHERE transaction_type = 'deposit' 
     GROUP BY account_id) d ON a.account_id = d.account_id
LEFT JOIN 
    (SELECT account_id, SUM(amount) AS total_withdrawals 
     FROM Transactions 
     WHERE transaction_type = 'withdrawal' 
     GROUP BY account_id) w ON a.account_id = w.account_id;

SELECT a.account_id, AVG(a.balance) AS avg_daily_balance
FROM Accounts a
JOIN Transactions t ON a.account_id = t.account_id
WHERE t.transaction_date BETWEEN '2024-09-01' AND '2024-09-30'
GROUP BY a.account_id;


SELECT account_type, SUM(balance) AS total_balance
FROM Accounts
GROUP BY account_type;


SELECT t.account_id, COUNT(t.transaction_id) AS transaction_count
FROM Transactions t
GROUP BY t.account_id
ORDER BY transaction_count DESC;


SELECT c.customer_id, c.first_name, c.last_name, a.account_type, SUM(a.balance) AS total_balance
FROM Customers c
JOIN Accounts a ON c.customer_id = a.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name, a.account_type
HAVING SUM(a.balance) > 100000;  


SELECT t.account_id, t.amount, t.transaction_date, COUNT(t.transaction_id) AS duplicate_count
FROM Transactions t
GROUP BY t.account_id, t.amount, t.transaction_date
HAVING COUNT(t.transaction_id) > 1;






--Tasks 4: Subquery and its type:
--1. Retrieve the customer(s) with the highest account balance.

SELECT * FROM Customers WHERE customer_id = (
	SELECT customer_id FROM Accounts WHERE balance = (
		SELECT MAX(balance) FROM Accounts
	)
);


--2. Calculate the average account balance for customers who have more than one account.

SELECT AVG(a.balance) AS avg_balance FROM Accounts a WHERE a.customer_id IN (
    SELECT customer_id FROM Accounts GROUP BY customer_id HAVING COUNT(account_id) > 1
);

--3. Retrieve accounts with transactions whose amounts exceed the average transaction amount.

SELECT t.account_id, t.amount FROM Transactions t WHERE t.amount > (
	SELECT AVG(amount) FROM Transactions
);

--4. Identify customers who have no recorded transactions.

SELECT c.customer_id, c.first_name, c.last_name FROM Customers c WHERE NOT EXISTS (
    SELECT * FROM Transactions t WHERE t.account_id IN (
        SELECT a.account_id FROM Accounts a WHERE a.customer_id = c.customer_id
    )
);


--5. Calculate the total balance of accounts with no recorded transactions.

SELECT SUM(a.balance) AS total_balance FROM Accounts a WHERE NOT EXISTS (
    SELECT * FROM Transactions t WHERE t.account_id = a.account_id
);

--6. Retrieve transactions for accounts with the lowest balance.

SELECT t.* FROM Transactions t WHERE t.account_id IN (
    SELECT account_id FROM Accounts WHERE balance = (
		SELECT MIN(balance) FROM Accounts
	)
);

--7. Identify customers who have accounts of multiple types.

SELECT customer_id, first_name, last_name FROM Customers WHERE customer_id IN (
    SELECT customer_id FROM Accounts GROUP BY customer_id
    HAVING COUNT(DISTINCT account_type) > 1
);

--8. Calculate the percentage of each account type out of the total number of accounts.

SELECT account_type, (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Accounts)) AS percentage
FROM Accounts GROUP BY account_type;

--9. Retrieve all transactions for a customer with a given customer_id.

SELECT * FROM Transactions WHERE account_id IN (
    SELECT account_id FROM Accounts WHERE customer_id = 1 
);
 

--10. Calculate the total balance for each account type, including a subquery within the SELECT 
--clause.

SELECT account_type, 
       (SELECT SUM(balance) FROM Accounts a2 WHERE a2.account_type = a.account_type) 
AS total_balance FROM Accounts a GROUP BY a.account_type;
