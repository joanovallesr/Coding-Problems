# 1971. Find if Path Exists in Graph

### Intuition
To determine if two nodes are connected in an undirected graph, we can treat each connected component as a "set." If two nodes belong to the same set, a path exists between them. The **Disjoint Set Union (DSU)** or **Union-Find** data structure is perfect for this, as it efficiently handles connectivity queries.

### Approach: Union-Find (DSU)
1. **Initialization:** Each node starts as its own parent (a forest of $n$ individual trees) with a size of 1.
2. **Union:** For every edge $(u, v)$, we perform a `union` operation. We find the roots of $u$ and $v$. If they are different, we attach the smaller tree under the larger tree (**Union by Size**) to keep the overall tree height small.
3. **Find:** The `find` operation traces the parent pointers up to the root.
4. **Result:** Finally, we check if `find(source) == find(destination)`. If they share the same root, they are in the same connected component.

### Complexity
* **Time Complexity:** $O(E \cdot \alpha(N))$, where $E$ is the number of edges and $\alpha$ is the Inverse Ackermann function. In practical terms, this is nearly **$O(1)$** per operation.
* **Space Complexity:** $O(N)$ to store the `parent` and `size` arrays.

### Implementation Highlights
- **Weighted Union:** By using the `size[]` array, we ensure the tree remains balanced, preventing the "long chain" problem that degrades performance to $O(N)$.
