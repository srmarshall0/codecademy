-- SELECT * FROM customers LIMIT 10;
-- SELECT * FROM orders LIMIT 10;
-- SELECT * FROM books LIMIT 10;

-- SELECT * FROM pg_indexes
-- WHERE tablename IN ('customers', 'orders', 'books');

-- EXPLAIN ANALYZE
-- SELECT customer_id, quantity
-- FROM orders
-- WHERE quantity > 18;

CREATE INDEX orders_customer_id_quantity ON orders(quantity)
WHERE quantity > 18;

-- EXPLAIN ANALYZE
-- SELECT customer_id, quantity
-- FROM orders
-- WHERE quantity > 18;

-- EXPLAIN ANALYZE
-- SELECT * FROM customers WHERE customer_id = 22695;               

ALTER TABLE customers
ADD PRIMARY KEY(customer_id);

-- EXPLAIN ANALYZE
-- SELECT * FROM customers WHERE customer_id = 22695;

-- SELECT * FROM pg_indexes
-- WHERE tablename IN ('customers', 'orders', 'books');


CLUSTER customers USING customers_pkey;

-- SELECT * FROM customers LIMIT 10;


CREATE INDEX orders_customer_id_book_id ON orders(customer_id, book_id);

DROP INDEX IF EXISTS orders_customer_id_book_id;

CREATE INDEX orders_customer_id_book_id_quantity ON orders(customer_id, book_id, quantity);

-- SELECT * FROM pg_indexes
-- WHERE tablename IN ('customers', 'orders', 'books');

CREATE INDEX books_author_title ON books(author, title);

EXPLAIN ANALYZE 
SELECT * FROM orders
WHERE quantity * price_base > 100;

CREATE INDEX orders_total_price_idx ON orders((quantity*price_base));

EXPLAIN ANALYZE
SELECT * FROM orders
WHERE quantity*price_base > 100;