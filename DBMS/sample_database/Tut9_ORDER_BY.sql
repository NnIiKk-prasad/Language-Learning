-- SELECT * FROM customers
-- ORDER BY country;

-- SELECT * FROM customers
-- ORDER BY country DESC;

-- SELECT * FROM customers
-- ORDER BY country, contactFirstName;

-- SELECT * FROM customers
-- ORDER BY country ASC, contactFirstName DESC;

-- These last two query may not work on other DBMS --

-- SELECT contactFirstName, contactLastName
-- FROM customers
-- ORDER BY country, contactFirstName;

-- SELECT contactFirstName, contactLastName, 10 AS points
-- FROM customers
-- ORDER BY points, contactFirstName;

# ---------Exercise-------------
SELECT *, (priceEach * quantityOrdered) AS total_price
FROM orderdetails
WHERE orderNumber = 10103
ORDER BY total_price DESC;