# 1148. Article Views I

[View Problem on LeetCode](https://leetcode.com/problems/article-views-i/)

**Difficulty:** Easy
**Topic:** Database

## Approach
The goal is to find all the authors who have viewed at least one of their own articles. 

1. **Filtering:** We use the `WHERE` clause to compare two columns within the same row (`author_id = viewer_id`). If they match, it means the person viewing the article is the person who wrote it.
2. **Deduplication:** Event log tables often contain duplicate actions (e.g., an author viewing their own article multiple times on different dates). To ensure we only return each author's ID once, we apply the `DISTINCT` keyword to the `SELECT` statement.
3. **Aliasing and Sorting:** Finally, we alias the output column to `id` as requested by the problem description and use `ORDER BY id` to sort the returned IDs in ascending order.

## Complexity Analysis
* **Time Complexity:** $O(n \log n)$ where $n$ is the number of rows in the `Views` table. The engine scans the table in $O(n)$ time to filter the rows, but the `ORDER BY` clause requires a sorting operation, which generally takes $O(n \log n)$ time.
* **Space Complexity:** $O(m)$ where $m$ is the number of unique authors who meet the criteria. This represents the memory required by the database engine to store the deduplicated and sorted result set before returning it.

## Code
The full solution is available in [`solution.sql`](./solution.sql).