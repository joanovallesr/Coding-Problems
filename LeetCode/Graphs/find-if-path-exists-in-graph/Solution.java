class Solution {
    // declare two instance variables to assign a parent and size to each tree
    private int[] parent;
    private int[] size;

    public boolean validPath(int n, int[][] edges, int source, int destination) {
        parent = new int[n];
        size = new int[n];

        // initially each node will point to itself, and we will have n trees of size 1
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
        // add each element of edges[][] to their correspondent root in sizes[]
        for (int[] edge: edges) {
            union(edge[0], edge[1]);
        }
        return find(source) == find(destination);
    }

    // trace the root
    private int find(int p) {
        while (p != parent[p]) {
            p = parent[p];
        }
        return p;
    }

    // attach the smaller tree to the bigger tree
    private void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        if (rootP == rootQ) {
            return;
        }
        if (size[rootP] > size[rootQ]) {
            parent[rootQ] = rootP;
            size[rootP] += size[rootQ];
        } else {
            parent[rootP] = rootQ;
            size[rootQ] += size[rootP];
        }
    }
}
