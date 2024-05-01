CREATE TABLE Customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15),
    address VARCHAR(255)
);


-- Create a new customer
INSERT INTO Customer (first_name, last_name, email, phone_number, address)
VALUES ('John', 'Doe', 'john.doe@example.com', '+1234567890', '123 Main St');

-- Read  all customers
SELECT * FROM Customer;

-- Read a specific customer by email
SELECT * FROM Customer WHERE email = 'john.doe@example.com';

-- Update customer's information
UPDATE Customer
SET phone_number = '+9876543210', address = '456 Elm St'
WHERE email = 'john.doe@example.com';

-- Delete a customer
DELETE FROM Customer WHERE email = 'john.doe@example.com';
