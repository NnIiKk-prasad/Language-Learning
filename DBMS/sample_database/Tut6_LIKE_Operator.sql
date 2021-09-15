-- SELECT * FROM customers
-- WHERE customerName LIKE 'a%';

-- SELECT * FROM customers
-- WHERE customerName LIKE 'asian%';

-- SELECT * FROM customers
-- WHERE customerName LIKE '%ltd';

-- SELECT * FROM customers
-- WHERE customerName LIKE '%gift%';

-- SELECT * FROM customers
-- WHERE contactLastName LIKE 'b%n';

-- SELECT * FROM customers
-- WHERE contactLastName LIKE '____n';

# ---------Exercise-------------
SELECT * FROM customers
WHERE addressLine1 LIKE '%street%' OR
	  addressLine1 LIKE '%avenue%';
