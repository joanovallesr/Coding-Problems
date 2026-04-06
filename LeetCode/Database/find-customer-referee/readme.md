# 584. Find Customer Referee

[View Problem on LeetCode](https://leetcode.com/problems/find-customer-referee/)

**Difficulty:** Easy
**Topic:** Database

## Approach
The goal is to retrieve the names of customers who were not referred by the customer with `referee_id = 2`. 

The core challenge of this problem is handling missing data (`NULL` values). In SQL, `NULL` represents an unknown value. If we only write the condition `WHERE referee_id != 2`, the database engine will evaluate any `NULL` records as `UNKNOWN` rather than `TRUE`, effectively filtering out customers who had no referee at all. 

To solve this, we must explicitly combine two conditions using the logical `OR` operator:
1. `referee_id != 2` (to catch customers referred by someone else)
2. `referee_id IS NULL` (to catch customers who were not referred by anyone)

## Complexity Analysis
* **Time Complexity:** $O(n)$ where $n$ is the number of rows in the `Customer` table. The database engine must perform a full table scan to evaluate both conditions against every row.
* **Space Complexity:** $O(m)$ where $m$ is the number of rows that satisfy the `WHERE` clause, representing the memory required to build and return the final result set.

## Code
The full solution is available in [`solution.sql`](./solution.sql).