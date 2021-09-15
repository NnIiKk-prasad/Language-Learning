-- SELECT *
-- FROM orders
-- INNER JOIN customers ON orders.customerNumber = customers.customerNumber;

-- SELECT orderNumber, contactFirstName, contactLastName
-- FROM orders
-- INNER JOIN customers ON orders.customerNumber = customers.customerNumber;

-- SELECT orderNumber, orders.customerNumber, contactFirstName, contactLastName
-- FROM orders
-- INNER JOIN customers ON orders.customerNumber = customers.customerNumber;

-- SELECT orderNumber, o.customerNumber, contactFirstName, contactLastName
-- FROM orders o
-- INNER JOIN customers c
-- ON o.customerNumber = c.customerNumber;

-- SELECT 
-- 	c.customerName, 
--     o.orderNumber, 
--     p.productName, 
--     od.quantityOrdered, 
--     od.priceEach,
--     p.productVendor
-- FROM orders o
-- JOIN customers c ON o.customerNumber = c.customerNumber
-- JOIN orderdetails od ON od.orderNumber = o.orderNumber
-- JOIN products p ON p.productCode = od.productCode;

# ---------Exercise-------------
SELECT orderNumber, p.productCode, productName, quantityOrdered, priceEach
FROM orderdetails od
JOIN products p ON p.productCode = od.productCode;
