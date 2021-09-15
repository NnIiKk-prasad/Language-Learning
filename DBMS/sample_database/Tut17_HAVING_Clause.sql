-- SELECT country, COUNT(customerNumber) AS 'No. of customers'
-- FROM customers
-- GROUP BY country
-- HAVING COUNT(customerNumber) > 5
-- ORDER BY COUNT(customerNumber) DESC;

SELECT c.customerName, COUNT(o.orderNumber) AS NumberOfOrders
FROM orders o
INNER JOIN customers c ON o.customerNumber = c.customerNumber
GROUP BY c.customerName
HAVING COUNT(o.orderNumber) > 10;
