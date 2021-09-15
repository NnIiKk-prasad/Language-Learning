-- SELECT a.customerName AS CustomerName1, b.customerName AS CustomerName2, a.city
-- FROM customers a, customers b
-- WHERE a.customerNumber <> b.customerNumber
-- AND a.city = b.city
-- ORDER BY a.city;

-- SELECT a.customerName AS CustomerName1, b.customerName AS CustomerName2, a.city
-- FROM customers a
-- JOIN customers b
-- 	ON a.customerNumber <> b.customerNumber AND a.city = b.city
-- ORDER BY a.city;

# ---------Exercise-------------
SELECT 
	e.employeeNumber,
    e.firstName,
    m.firstName AS manager
FROM employees e
LEFT JOIN employees m
	ON e.reportsTo = m.employeeNumber
