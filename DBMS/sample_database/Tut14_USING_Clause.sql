SELECT 
	o.orderNumber, 
    c.contactFirstName,
    p.productVendor
FROM orders o
JOIN customers c USING (customerNumber)
JOIN orderdetails od USING (orderNumber)
JOIN products p USING (productCode)
