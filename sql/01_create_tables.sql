CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(50)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category_id INT,
    brand VARCHAR(50),
    rating DECIMAL(2,1),
    price DECIMAL(10,2),
    stock_quantity INT,
    discount_percentage INT,
    cost_price DECIMAL(10,2),

    CONSTRAINT fk_product_category
    FOREIGN KEY (category_id)
    REFERENCES categories(category_id)
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50),
    signup_date DATE,
    gender VARCHAR(10),
    age INT,
    customer_segment VARCHAR(30)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    shipping_city VARCHAR(50),
    order_status VARCHAR(20),
    total_amount DECIMAL(10,2),

    CONSTRAINT fk_order_customer
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2),
    discount_percentage INT,
    final_price DECIMAL(10,2),

    CONSTRAINT fk_item_order
    FOREIGN KEY (order_id)
    REFERENCES orders(order_id),

    CONSTRAINT fk_item_product
    FOREIGN KEY (product_id)
    REFERENCES products(product_id)
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    order_id INT,
    payment_method VARCHAR(30),
    payment_status VARCHAR(20),
    payment_date DATE,
    transaction_amount DECIMAL(10,2),

    CONSTRAINT fk_payment_order
    FOREIGN KEY (order_id)
    REFERENCES orders(order_id)
);