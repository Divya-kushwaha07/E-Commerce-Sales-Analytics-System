-- Find customers who have placed more than 10 orders

SELECT
    customer_id,
    COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 10
ORDER BY total_orders DESC;


-- Categorize orders based on total amount

SELECT
    order_id,
    total_amount,
    CASE
        WHEN total_amount >= 100000 THEN 'High Value'
        WHEN total_amount >= 50000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS order_category
FROM orders;


-- Find products priced above average price

SELECT
    product_name,
    price
FROM products
WHERE price >
(
    SELECT AVG(price)
    FROM products
);


-- Find customers whose total spending is above average spending

SELECT
    customer_id,
    customer_name
FROM customers c
WHERE
(
    SELECT SUM(total_amount)
    FROM orders o
    WHERE o.customer_id = c.customer_id
)
>
(
    SELECT AVG(total_amount)
    FROM orders
);


-- Find top 10 customers by spending

WITH customer_spending AS
(
    SELECT
        customer_id,
        SUM(total_amount) AS total_spent
    FROM orders
    GROUP BY customer_id
)

SELECT
    customer_id,
    total_spent
FROM customer_spending
ORDER BY total_spent DESC
LIMIT 10;


