# 1683. Invalid Tweets

[View Problem on LeetCode](https://leetcode.com/problems/invalid-tweets/)

**Difficulty:** Easy
**Topic:** Database

## Approach
The objective is to find the IDs of all tweets that exceed a strict 15-character limit. 

To filter these records, we use a `WHERE` clause combined with a string length function. The critical design choice here is using `CHAR_LENGTH()` rather than `LENGTH()`.

**`CHAR_LENGTH()` vs. `LENGTH()`:**
In MySQL, `LENGTH()` returns the length of a string measured in *bytes*. `CHAR_LENGTH()` returns the length of the string measured in *characters*. 
In modern applications, users frequently use emojis or characters from various global alphabets. An emoji might only count as 1 character, but it can take up 3 or 4 bytes of storage. If we used `LENGTH()`, a tweet with 4 emojis might be incorrectly flagged as exceeding 15 characters because its byte size is too large. `CHAR_LENGTH()` ensures we are strictly counting the human-readable characters, making the query perfectly robust for real-world text data.

## Complexity Analysis
* **Time Complexity:** $O(n)$ where $n$ is the total number of rows in the `Tweets` table. Because we are applying a function to the `content` column, the database engine cannot rely on standard indexing and must perform a full table scan to evaluate every row.
* **Space Complexity:** $O(m)$ where $m$ is the number of rows that satisfy the condition, representing the memory allocated by the database to return the matching `tweet_id` records.

## Code
The full solution is available in [`solution.sql`](./solution.sql).