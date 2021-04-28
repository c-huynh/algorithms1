# Homework 5

## Dijkstra's Algorithm

Implementation of Djikstra's shortest path algorithm with min heap.

The file (dijkstraData.txt) contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a vertex v and vertex 1, we'll define the shortest-path distance between 1 and v to be 1000000.

You should report the shortest-path distances to the following ten vertices, in order: 7, 37, 59, 82, 99, 115, 133, 165, 188, 197. Enter the shortest-path distances using the fields below for each of the vertices.

### Answers

*Shortest path to 7 = 2599*

*Shortest path to 37 = 2610*

*Shortest path to 59 = 2947*

*Shortest path to 82 = 2052*

*Shortest path to 99 = 2367*

*Shortest path to 115 = 2399*

*Shortest path to 133 = 2029*

*Shortest path to 165 = 2442*

*Shortest path to 188 = 2505*

*Shortest path to 197 = 3068*