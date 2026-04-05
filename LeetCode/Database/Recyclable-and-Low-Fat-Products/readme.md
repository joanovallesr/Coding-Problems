# 1757. Recyclable and Low Fat Products

[View Problem on LeetCode](https://leetcode.com/problems/recyclable-and-low-fat-products/)

**Difficulty:** Easy
**Topic:** Database

## Approach
This is a straightforward data retrieval problem. We need to query the `Products` table to find specific items that meet two exact conditions simultaneously. 

By using the `SELECT` statement, we isolate the `product_id` column. We then apply a `WHERE` clause combined with the logical `AND` operator to filter the records. This ensures the database engine only returns rows where the `low_fats` flag is 'Y' and the `recyclable` flag is also 'Y'.

## Complexity Analysis
* **Time Complexity:** $O(n)$ where $n$ is the number of rows in the `Products` table. Assuming no specific indexes exist on these columns, the database engine must perform a full table scan to check every row against our conditions.
* **Space Complexity:** $O(m)$ where $m$ is the number of rows that satisfy both conditions, representing the memory required to store and return the final result set.

## Code
The full solution is available in [`solution.sql`](./solution.sql).