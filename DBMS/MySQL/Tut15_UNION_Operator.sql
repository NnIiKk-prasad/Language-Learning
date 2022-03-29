-- SELECT
-- 	orderNumber,
--     orderDate,
--     'Active' AS status
-- FROM orders
-- WHERE orderDate >= '2005-01-01'
-- UNION
-- SELECT
-- 	orderNumber,
--     orderDate,
--     'Archieved' AS status
-- FROM orders
-- WHERE orderDate < '2005-01-01';

# ---------Exercise-------------
SELECT 
	customerNumber,
	customerName,
    creditLimit,
    'Bronze' AS type
FROM customers
WHERE creditLimit < 50000
UNION
SELECT 
	customerNumber,
	customerName,
    creditLimit,
    'Silver' AS type
FROM customers
WHERE creditLimit BETWEEN 50000 AND 100000
UNION
SELECT 
	customerNumber,
	customerName,
    creditLimit,
    'Gold' AS type
FROM customers
WHERE creditLimit > 100000
ORDER BY customerName;
