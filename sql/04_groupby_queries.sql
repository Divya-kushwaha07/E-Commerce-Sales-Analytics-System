-- Calculate total revenue by payment method

SELECT
    payment_method,
    ROUND(SUM(transaction_amount), 2) AS revenue
FROM payments
WHERE payment_status = 'Success'
GROUP BY payment_method
ORDER BY revenue DESC;


-- Count orders by status

SELECT
    order_status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;


-- Count customers by segment

SELECT
    customer_segment,
    COUNT(*) AS total_customers
FROM customers
GROUP BY customer_segment
ORDER BY total_customers DESC;


-- Average customer age by gender

SELECT
    gender,
    ROUND(AVG(age), 2) AS average_age
FROM customers
GROUP BY gender;
