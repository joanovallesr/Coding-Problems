-- 595. Big Countries
-- Time Complexity: O(n) - The database engine scans the table to find matching rows. 
-- (Note: In a real-world scenario with indexes on 'area' and 'population', UNION can optimize this to O(log n)).
-- Space Complexity: O(m) - Where m is the number of rows returned that meet the criteria.

SELECT name, population, area
  FROM World
 WHERE population >= 25000000

 UNION

SELECT name, population, area
  FROM World
 WHERE area >= 3000000;