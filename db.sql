-- 1. Create Customers Table
CREATE TABLE customers (
    customer_id INT NOT NULL PRIMARY KEY,
    name NVARCHAR(255) NULL,
    email NVARCHAR(255) NULL,
    created_at DATETIME2 NULL DEFAULT GETDATE()
);

-- 2. Create Orders Table
CREATE TABLE orders (
    order_id INT NOT NULL PRIMARY KEY,
    customer_id INT NULL,
    order_date DATE NULL,
    total_amount DECIMAL(18, 2) NULL,
    -- Define Foreign Key relationship
    CONSTRAINT FK_Orders_Customers FOREIGN KEY (customer_id) 
        REFERENCES customers(customer_id)
);

-- 3. Insert Sample Records
INSERT INTO customers (customer_id, name, email, created_at)
VALUES 
(1, 'Alice Johnson', 'alice@example.com', '2023-01-15 10:30:00'),
(2, 'Bob Smith', 'bob@example.com', '2023-02-20 14:45:00'),
(3, 'Charlie Brown', 'charlie@example.com', '2023-03-05 09:15:00');
(4, 'Diana Prince', 'diana@themyscira.com', '2023-07-12 08:00:00'),
(5, 'Edward Nigma', 'riddler@gotham.com', '2023-08-01 11:20:00'),
(6, 'Fiona Gallagher', 'fiona@southside.com', '2023-09-14 16:30:00'),
(7, 'George Costanza', 'art_vandelay@latex.com', '2023-10-10 12:00:00'),
(8, 'Hannah Abbott', 'hannah@hufflepuff.edu', '2023-11-22 09:45:00'),
(9, 'Ian Malcolm', 'chaos@jurassic.org', '2023-12-05 13:10:00'),
(10, 'Julia Child', 'cooking@french.com', '2024-01-10 15:55:00');


INSERT INTO orders (order_id, customer_id, order_date, total_amount)
VALUES 
(101, 1, '2023-04-01', 150.50),
(102, 1, '2023-04-15', 89.99),
(103, 2, '2023-05-20', 210.00),
(104, 3, '2023-06-10', 45.00);
(105, 4, '2023-07-20', 500.00),
(106, 5, '2023-08-05', 12.50),
(107, 5, '2023-08-15', 35.75),
(108, 6, '2023-09-20', 99.99),
(109, 1, '2023-10-01', 25.00), -- Customer 1 again
(110, 2, '2023-11-05', 300.25), -- Customer 2 again
(111, 7, '2023-12-01', 15.00),
(112, 4, '2023-12-15', 750.00), -- High value order
(113, 8, '2024-01-05', 62.40),
(114, 10, '2024-01-20', 120.00),
(115, 1, '2024-02-01', 10.00),  -- Recent order
(116, 5, '2024-02-10', 55.00);