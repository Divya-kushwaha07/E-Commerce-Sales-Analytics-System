-- Assign a unique rank to customers based on total spending

SELECT
    customer_id,
    SUM(total_amount) AS total_spent,
    ROW_NUMBER() OVER (
        ORDER BY SUM(total_amount) DESC
    ) AS row_num
FROM orders
GROUP BY customer_id;


-- Rank customers based on total spending

SELECT
    customer_id,
    SUM(total_amount) AS total_spent,
    RANK() OVER (
        ORDER BY SUM(total_amount) DESC
    ) AS customer_rank
FROM orders
GROUP BY customer_id;


-- Dense rank customers based on total spending

SELECT
    customer_id,
    SUM(total_amount) AS total_spent,
    DENSE_RANK() OVER (
        ORDER BY SUM(total_amount) DESC
    ) AS dense_rank
FROM orders
GROUP BY customer_id;


-- Divide customers into four spending groups

SELECT
    customer_id,
    SUM(total_amount) AS total_spent,
    NTILE(4) OVER (
        ORDER BY SUM(total_amount) DESC
    ) AS spending_group
FROM orders
GROUP BY customer_id;


-- Calculate cumulative revenue by order date

SELECT
    order_date,
    SUM(total_amount) AS daily_revenue,

    SUM(
        SUM(total_amount)
    ) OVER (
        ORDER BY order_date
    ) AS running_total
FROM orders
GROUP BY order_date
ORDER BY order_date;


-- Calculate 3-day moving average revenue

SELECT
    order_date,
    SUM(total_amount) AS daily_revenue,

    ROUND(
        AVG(
            SUM(total_amount)
        ) OVER (
            ORDER BY order_date
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS moving_average
FROM orders
GROUP BY order_date
ORDER BY order_date;