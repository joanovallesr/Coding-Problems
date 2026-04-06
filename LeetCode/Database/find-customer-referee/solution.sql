-- 584. Find Customer Referee
-- Time Complexity: O(n) - Full table scan to evaluate every customer record.
-- Space Complexity: O(m) - Where m is the number of matching records returned.

SELECT name
  FROM Customer
 WHERE referee_id != 2
    OR referee_id IS NULL;