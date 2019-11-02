"""
Implementation of Djikstra's shortest path algorithm with min heap.

The file (dijkstraData.txt) contains an adjacency list representation of an
undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists
of the node tuples that are adjacent to that particular vertex along with the
length of that edge. For example, the 6th row has 6 as the first entry indicating
that this row corresponds to the vertex labeled 6. The next entry of this row
"141,8200" indicates that there is an edge between vertex 6 and vertex 141 that
has length 8200. The rest of the pairs of this row indicate the other vertices
adjacent to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1
(the first vertex) as the source vertex, and to compute the shortest-path distances
between 1 and every other vertex of the graph. If there is no path between a vertex
v and vertex 1, we'll define the shortest-path distance between 1 and v to be 1000000.

You should report the shortest-path distances to the following ten vertices, in
order: 7, 37, 59, 82, 99, 115, 133, 165, 188, 197. Enter the shortest-path
distances using the fields below for each of the vertices.
"""

class min_heap(object):
    def __init__(self, A):
        
        # heap array has empty first element
        self.heap = self.build_min_heap(A)
        self.size = len(self.heap) - 1

    def heapify(self, A, i):
        # i is the root to heapify from
        n = len(A)
        smallest = i
        l = 2 * i
        r = 2 * i + 1

        if (l < n) and (A[l] < A[smallest]):
            smallest = l
        if (r < n) and (A[r] < A[smallest]):
            smallest = r
        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
            self.heapify(A, smallest)

    def build_min_heap(self, A):
        A = [None] + A
        n = len(A)//2
        for i in range(n, 0, -1):
            self.heapify(A, i)
        return A

    def bubble_up(self, i):
        # i is the index of node to bubble up
        parent = i // 2
        while (parent > 0) and (self.heap[parent] > self.heap[i]):
            self.heap[parent], self.heap[i] = \
            self.heap[i], self.heap[parent]
            i = parent
            parent = i // 2

    def insert(self, i):
        # add to end of heap
        self.heap.append(i)
        self.size += 1

        # bubble up to restore heap invariants
        i = self.size
        self.bubble_up(i)

    def extract_min(self):
        if self.size >= 1:
            # swap root and bottom-most, right-most child and remove last element
            child = self.size
            self.heap[1], self.heap[child] = self.heap[child], self.heap[1]
            min = self.heap.pop()
            self.size -= 1

            # restore heap invariants
            self.heapify(self.heap, 1)
            return min
        else:
            return None

    def delete(self, i):
        # i is the index of node to delete
        if self.size >= 1:
            child = heap.size
            self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
            self.heap.pop()

            # restore heap invariants
            if (i != child):
                self.bubble_up(i)
                self.heapify(self.heap, i)
            self.size -= 1


input_file = "dijkstraData.txt"
source = 1

graph = {}               # adjacency list
shortest_path = [None]   # shortest path (index correspond to node)

# create adjacency list
with open(input_file, "r") as f:
    for line in f:

        # extract nodes
        i = line.split()
        graph[int(i[0])] = []

        # extract edges
        iter_i = iter(i)
        next(iter_i)
        for j in iter_i:
            edge = j.split(",")
            graph[int(i[0])].append((int(edge[0]), int(edge[1])))

n_nodes = len(graph)

# initialize Djiktra lists
shortest_path += [None] * n_nodes
queue = min_heap([(0, source)])

while queue.size > 0:
    path_length, v = queue.extract_min()
    if shortest_path[v] == None:
        shortest_path[v] = path_length
        for w, edge_length in graph[v]:
            if shortest_path[w] == None:
                queue.insert((path_length + edge_length, w))

print("shortest path to 7 = " + str(shortest_path[7]))       # answer = 2599
print("shortest path to 37 = " + str(shortest_path[37]))     # answer = 2610
print("shortest path to 59 = " + str(shortest_path[59]))     # answer = 2947
print("shortest path to 82 = " + str(shortest_path[82]))     # answer = 2052
print("shortest path to 99 = " + str(shortest_path[99]))     # answer = 2367
print("shortest path to 115 = " + str(shortest_path[115]))   # answer = 2399
print("shortest path to 133 = " + str(shortest_path[133]))   # answer = 2029
print("shortest path to 165 = " + str(shortest_path[165]))   # answer = 2442
print("shortest path to 188 = " + str(shortest_path[188]))   # answer = 2505
print("shortest path to 197 = " + str(shortest_path[197]))   # answer = 3068
