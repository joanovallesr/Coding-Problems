-- 1683. Invalid Tweets
-- Time Complexity: O(n) - A full table scan is required to evaluate the length 
-- of the 'content' column for every tweet in the table.
-- Space Complexity: O(m) - Where m is the number of invalid tweets (length > 15) 
-- that are returned in the final result set.

SELECT tweet_id
  FROM Tweets
 WHERE CHAR_LENGTH(content) > 15;