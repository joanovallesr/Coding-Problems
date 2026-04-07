# 595. Big Countries

[View Problem on LeetCode](https://leetcode.com/problems/big-countries/)

**Difficulty:** Easy
**Topic:** Database

## Approach
A country is considered "big" if it meets at least one of two criteria: 
1. Its area is at least 3,000,000 $km^2$.
2. Its population is at least 25,000,000.

While the simplest way to write this query is by using a single `WHERE` clause with an `OR` operator, this solution utilizes the `UNION` operator to combine the results of two separate `SELECT` statements.

**Why `UNION`?** In large-scale databases, using an `OR` condition on two different columns can sometimes confuse the query optimizer, causing it to ignore available indexes and perform a slow, full table scan. By breaking it into two distinct queries and using `UNION`, the database can independently utilize the index on `population` for the first query and the index on `area` for the second. `UNION` automatically removes any duplicate rows (e.g., a country that is both massive in area and population) before returning the final result set.

## Complexity Analysis
* **Time Complexity:** $O(n)$ where $n$ is the number of rows in the `World` table. Assuming no indexes, the engine must scan the table for both queries. (If properly indexed, the `UNION` approach can reduce the time complexity closer to $O(\log n)$).
* **Space Complexity:** $O(m)$ where $m$ is the number of distinct countries that satisfy either condition, representing the memory needed to store the merged result set.

## Code
The full solution is available in [`solution.sql`](./solution.sql).