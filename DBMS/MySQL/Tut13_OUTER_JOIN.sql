-- SELECT 
-- 	c.customerNumber, 
--     c.contactFirstName, 
--     o.orderNumber
-- FROM orders o
-- LEFT OUTER JOIN customers c 
-- 	ON o.customerNumber = c.customerNumber;

-- SELECT 
-- 	c.customerNumber, 
--     c.contactFirstName, 
--     o.orderNumber
-- FROM orders o
-- LEFT JOIN customers c 
-- 	ON o.customerNumber = c.customerNumber;

-- SELECT 
-- 	c.customerName, 
--     o.orderNumber, 
--     p.productName, 
--     od.quantityOrdered, 
--     od.priceEach,
--     p.productVendor
-- FROM orders o
-- LEFT JOIN customers c ON o.customerNumber = c.customerNumber
-- LEFT JOIN orderdetails od ON od.orderNumber = o.orderNumber
-- LEFT JOIN products p ON p.productCode = od.productCode;

# ---------Exercise-------------
SELECT 
	p.productCode,
    p.productName,
    od.quantityOrdered
FROM products p
LEFT JOIN orderdetails od
	ON 	p.productCode = od.productCode;
