CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(20)
);

INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone)
VALUES (1, 'John', 'Smith', 'john.smith@example.com', '(555) 555-1234'),
       (2, 'Jane', 'Doe', 'jane.doe@example.com', '(555) 555-5678'),
       (3, 'Bob', 'Johnson', 'bob.johnson@example.com', '(555) 555-9012'),
       (4, 'Emily', 'Davis', 'emily.davis@example.com', '(555) 555-3456'),
       (5, 'Tom', 'Wilson', 'tom.wilson@example.com', '(555) 555-7890');

--query1
select FirstName, LastName, Email
from Customers

--query2
select Phone
from Customers
where CustomerID='3';

--query3
select count(CustomerID) as TotalCustomer
from Customers

--query4
select * 
from Customers
where FirstName LIKE 'J%';

--query5
select Email
from Customers
where LastName = 'Wilson';

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount)
VALUES (1, 1, '2022-01-01', 100.00),
       (2, 1, '2022-02-01', 200.00),
       (3, 2, '2022-02-15', 50.00),
       (4, 3, '2022-03-01', 75.00),
       (5, 4, '2022-04-01', 150.00);

--query1
select OrderID, TotalAmount
from Orders

--query2
select sum(TotalAmount) as Sum_of_all_amount
from Orders

--query3
select OrderDate, TotalAmount
from Orders
where OrderID='3';

--query4
