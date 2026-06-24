COPY categories
FROM 'C:\Users\Hp\Desktop\DataScienceLearn\Projects\E-Commerce Sales Analytics System\data\categories.csv'
DELIMITER ','
CSV HEADER;

COPY products
FROM 'C:\Users\Hp\Desktop\DataScienceLearn\Projects\E-Commerce Sales Analytics System\data\products.csv'
DELIMITER ','
CSV HEADER;

COPY customers
FROM 'C:\Users\Hp\Desktop\DataScienceLearn\Projects\E-Commerce Sales Analytics System\data\customers.csv'
DELIMITER ','
CSV HEADER;

COPY orders
FROM 'C:\Users\Hp\Desktop\DataScienceLearn\Projects\E-Commerce Sales Analytics System\data\orders.csv'
DELIMITER ','
CSV HEADER;

COPY order_items
FROM 'C:\Users\Hp\Desktop\DataScienceLearn\Projects\E-Commerce Sales Analytics System\data\order_items.csv'
DELIMITER ','
CSV HEADER;

COPY payments
FROM 'C:\Users\Hp\Desktop\DataScienceLearn\Projects\E-Commerce Sales Analytics System\data\payments.csv'
DELIMITER ','
CSV HEADER;