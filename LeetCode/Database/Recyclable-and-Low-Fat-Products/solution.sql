-- 1757. Recyclable and Low Fat Products
-- Time Complexity: O(n) - Full table scan (assuming no indexes).
-- Space Complexity: O(m) - Where m is the number of matching rows returned.

SELECT product_id
  FROM Products
 WHERE low_fats = 'Y'
   AND recyclable = 'Y';