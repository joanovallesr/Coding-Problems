# 332. Reconstruct Itinerary

[View Problem on LeetCode](https://leetcode.com/problems/reconstruct-itinerary/)

**Difficulty:** Hard
**Topic:** Graphs

## Approach
This problem asks us to find an **Eulerian Path** in a directed graph (a path that visits every edge exactly once), with the added constraint that we must return the lexicographically smallest itinerary if multiple valid paths exist.

A greedy Depth-First Search (DFS) might fail here. If we always pick the alphabetically smallest destination, we might travel into a "dead-end" airport before we have visited all the other interconnected airports, leaving tickets unused. 

To solve this, we use **Hierholzer’s Algorithm**:
1. **Min-Heap Graph:** We build an adjacency list where the destinations are stored in a Priority Queue (Min-Heap). This guarantees that we always attempt to visit destinations in alphabetical order.
2. **Post-Order DFS:** We traverse the graph. If we reach an airport that has no more outgoing flights, we are at a dead end. Instead of failing, we append this dead-end airport to our `route` array and backtrack. 
3. Because we only add airports to our route *after* exhausting all their outgoing flights, the "dead end" is safely recorded as the very last stop. 
4. **Reverse the Result:** Since the route was constructed backwards (from the final dead-end up to the starting point), we simply reverse the `route` array at the end to get the correct chronological itinerary.

## Complexity Analysis
* **Time Complexity:** $O(E \log E)$ where $E$ is the number of tickets (edges). Inserting $E$ tickets into min-heaps takes $O(E \log E)$ time. During the DFS, we visit each edge exactly once, and extracting the minimum element from a heap takes $O(\log E)$ time, leading to $O(E \log E)$ for the traversal. 
* **Space Complexity:** $O(V + E)$ where $V$ is the number of airports and $E$ is the number of tickets. This accounts for the memory required to store the adjacency list graph and the maximum depth of the DFS recursion stack.

## Code
The full solution is available in [`solution.py`](./solution.py).