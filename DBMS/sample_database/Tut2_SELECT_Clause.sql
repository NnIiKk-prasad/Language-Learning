-- SELECT 
-- 	contactFirstName,
--     contactLastName,
--     creditLimit,
--     creditLimit + creditLimit % 10000 AS 'new creditLimit'
-- FROM customers;

-- SELECT DISTINCT country FROM customers;

-- SELECT COUNT(DISTINCT country) FROM customers;

-- SELECT country, COUNT(country) FROM customers GROUP BY country;

# ---------Exercise-------------
SELECT 
	productName,
    MSRP,
    MSRP * 1.1 AS 'NEW MSRP'
FROM products;