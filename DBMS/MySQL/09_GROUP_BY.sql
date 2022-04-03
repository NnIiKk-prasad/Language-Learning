-- SELECT country, COUNT(customerNumber) AS 'No. of customers'
-- FROM customers
-- GROUP BY country
-- ORDER BY COUNT(customerNumber) DESC;

-- SELECT 
--     productLine,
--     MIN(MSRP) AS smallestPrice,
--     MAX(MSRP) AS largestPrice,
-- 	AVG(MSRP) AS averagePrice,
--     SUM(quantityInStock) AS totalQuantity
-- FROM products
-- GROUP BY productLine;

# ---------Exercise-------------
SELECT 
    orderNumber,
    SUM(quantityOrdered) AS 'Total quantity ordered',
    SUM(quantityOrdered * priceEach) AS 'Total Price'
FROM orderdetails
GROUP BY orderNumber;
