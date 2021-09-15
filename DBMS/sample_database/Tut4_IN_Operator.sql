-- SELECT * FROM customers
-- WHERE country IN ('Germany', 'France', 'UK');

-- SELECT * FROM customers
-- WHERE country NOT IN ('Germany', 'France', 'UK');

-- SELECT * FROM customers
-- WHERE country IN (SELECT country FROM offices);

# ---------Exercise-------------
SELECT * FROM products
WHERE quantityInStock IN (548, 992, 45);
