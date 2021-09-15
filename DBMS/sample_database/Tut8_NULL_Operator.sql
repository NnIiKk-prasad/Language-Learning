-- SELECT customerName, phone, addressLine1
-- FROM customers
-- WHERE state IS NULL;

-- SELECT customerName, phone, addressLine1
-- FROM customers
-- WHERE state IS NOT NULL;

# ---------Exercise-------------
SELECT * FROM orders
WHERE shippedDate IS NULL;