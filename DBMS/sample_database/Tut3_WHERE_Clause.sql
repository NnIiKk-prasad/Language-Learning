-- SELECT * FROM customers
-- WHERE country = 'Canada';

-- SELECT * FROM products
-- WHERE quantityInStock <= 1000;

-- SELECT * FROM orders
-- WHERE orderDate >= '2004-01-01' AND orderDate <= '2004-12-31';

-- SELECT * FROM customers
-- WHERE country = 'USA' AND City = 'NYC';

-- SELECT * FROM customers
-- WHERE city = 'Berlin' OR city = 'München';

-- SELECT * FROM customers
-- WHERE country = 'USA' AND city = 'NYC' OR city = 'Auckland';

-- SELECT * FROM customers
-- WHERE country = 'USA' AND (city = 'NYC' OR city = 'Auckland');

-- SELECT * FROM customers
-- WHERE NOT country = 'Germany' AND NOT country = 'USA';

# ---------Exercise-------------
SELECT * FROM orderdetails
WHERE orderNumber = 10103 AND priceEach * quantityOrdered > 5000;
