# Homework 4
## Strongly Connected Components

The file contains the edges of a directed graph. Vertices are labeled as positive integers from to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646.

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.

Enter the sizes of the 5 largest SCCs in the given graph using the fields below, in decreasing order of sizes. So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, enter 500 in the first field, 400 in the second, 300 in the third, and so on. If your algorithm finds less than 5 SCCs, then enter 0 for the remaining fields. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then you enter 400, 300, and 100 in the first, second, and third fields, respectively, and 0 in the remaining 2 fields.

`python scc.py`

### Answers

*largest SCC = 434821*

*second SCC = 968*

*third SCC = 459*

*fourth SCC = 313*

*fifth SCC = 211*