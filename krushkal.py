class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    edges = [(cost, u, v) for u, adj in graph.items() for v, cost in adj]
    edges.sort()

    mst = []
    disjoint_set = DisjointSet(graph.keys())

    for cost, u, v in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            mst.append((u, v, cost))
            disjoint_set.union(u, v)

    return mst

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(kruskal(graph))

Output: 

[('A', 'B', 1), ('C', 'D', 1), ('B', 'C', 2)]

