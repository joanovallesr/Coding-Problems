from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        332. Reconstruct Itinerary
        
        Time Complexity: O(E log E) - Where E is the number of edges (tickets). 
        Building the graph takes O(E log E) due to heap insertions. The DFS visits 
        each edge exactly once, and popping from the heap takes O(log E) time.
        Space Complexity: O(V + E) - Where V is the number of airports (vertices) 
        and E is the number of flights (edges). This space is used by the adjacency 
        list and the DFS call stack.
        """
        # Step 1: Build an adjacency list where each destination list is a Min-Heap.
        # This ensures we always visit lexical neighbors first.
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        route = []
        
        # Step 2: Post-Order DFS to traverse the graph (Hierholzer's Algorithm)
        def dfs(airport: str) -> None:
            pq = graph[airport]
            # While there are outgoing flights from this airport
            while pq:
                # Greedily pick the alphabetically smallest destination
                next_stop = heapq.heappop(pq)
                dfs(next_stop)
            # When an airport has no more outgoing flights (a dead end), 
            # we add it to our route.
            route.append(airport)

        # Step 3: Start the traversal from JFK
        dfs("JFK")
        
        # Because we appended nodes at their dead-ends, the route is built backwards.
        # We must reverse it to get the correct chronological itinerary.
        return route[::-1]