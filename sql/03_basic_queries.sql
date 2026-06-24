-- Calculate total revenue from successful payments

SELECT
    ROUND(SUM(transaction_amount), 2) AS total_revenue
FROM payments
WHERE payment_status = 'Success';


-- Count total customers

SELECT
    COUNT(*) AS total_customers
FROM customers;


-- Count total orders

SELECT
    COUNT(*) AS total_orders
FROM orders;


-- Calculate average order value

SELECT
    ROUND(AVG(total_amount), 2) AS average_order_value
FROM orders;




