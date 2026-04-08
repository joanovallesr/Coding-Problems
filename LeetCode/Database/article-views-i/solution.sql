-- 1148. Article Views I
-- Time Complexity: O(n log n) - The database must perform a full table scan O(n) 
-- to find matches, and then sort the results O(n log n) due to the ORDER BY clause.
-- Space Complexity: O(m) - Where m is the number of distinct authors who viewed 
-- their own articles, representing the memory needed for the final result set.

SELECT DISTINCT author_id AS id
  FROM Views
 WHERE author_id = viewer_id
 ORDER BY id;