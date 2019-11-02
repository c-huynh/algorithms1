"""
The file contains the edges of a directed graph. Vertices are labeled as positive
integers from 1 to 875714. Every row indicates an edge, the vertex label in first
column is the tail and the vertex label in second column is the head (recall the
graph is directed, and the edges are directed from the first column vertex to the
second column vertex). So for example, the 11th row looks liks : "2 47646". This
just means that the vertex with label 2 has an outgoing edge to the vertex with
label 47646.

Your task is to code up the algorithm from the video lectures for computing strongly
connected components (SCCs), and to run this algorithm on the given graph.

Enter the sizes of the 5 largest SCCs in the given graph using the fields below,
in decreasing order of sizes. So if your algorithm computes the sizes of the five
largest SCCs to be 500, 400, 300, 200 and 100, enter 500 in the first field, 400
in the second, 300 in the third, and so on. If your algorithm finds less than 5
SCCs, then enter 0 for the remaining fields. Thus, if your algorithm computes only
3 SCCs whose sizes are 400, 300, and 100, then you enter 400, 300, and 100 in the
first, second, and third fields, respectively, and 0 in the remaining 2 fields.
"""

def get_finishing_time(g, visited, i):
    visited[i-1] = True
    for j in g[i]:
        if visited[j-1] == False:
            get_finishing_time(g, visited, j)
    finishing_times.append(i)

def count_SCC_size(graph, visited, i):
    global size

    visited[i-1] = True
    size += 1
    for j in graph[i]:
        if visited[j-1] == False:
            count_SCC_size(graph, visited, j)

def get_finishing_time_iteratively(g, visited, i, finishing_times):
    stack = [i]

    while stack:
        node = stack[-1]

        # node visited first time
        # add all unvisited adjacent vertices to stack
        if visited[node-1] == 0:
            visited[node-1] += 1
            for j in g[node]:
                if visited[j-1] == 0:
                    stack.append(j)

        # node visited second time
        # only pop node from stack after 2nd visit
        elif visited[node-1] == 1:
            visited[node-1] += 1
            finishing_times.append(node)
            stack.pop()
        else:
            stack.pop()

def count_SCC_iteratively(g, visited, i, SCC_sizes):
    size = 0
    stack = []
    if visited[i-1] == False:
        stack = [i]
    while stack:
        node = stack.pop()
        if visited[node-1] == False:
            visited[node-1] = True
            size += 1
        for j in graph[node]:
            if visited[j-1] == False:
                stack.append(j)
    if size > 0:
        SCC_sizes.append(size)

# create graphs
N = 875714
graph = {}
graph_reversed = {}
for i in range(1, N+1):
    graph[i] = []
    graph_reversed[i] = []
print("creating graphs...")

# add edges
with open("SCC.txt", "r") as f:
    for line in f:
        edge = line.split()
        graph[int(edge[0])].append(int(edge[1]))
        graph_reversed[int(edge[1])].append(int(edge[0]))
print("adding edges...")

# first pass (using iteration instead of recursion)
finishing_times = []
n = len(graph_reversed)
visited = [0] * n # keep track of how many times node has been visited
for i in range(n, 0, -1):
    if visited[i-1] == 0:
        get_finishing_time_iteratively(graph_reversed, visited, i, finishing_times)
print("finished first pass...")

# second pass (using iteration instead of recursion)
SCC_sizes = []
visited = [False] * n
while finishing_times:
    i = finishing_times.pop()
    count_SCC_iteratively(graph, visited, i, SCC_sizes)
    # print("")
print("finishing second pass...")

print(sorted(SCC_sizes, reverse=True)[:5])

# answer 
# largest SCC = 434821
# second largest SCC = 968
# third largest SCC = 459
# fourth largest SCC = 313
# fifth largest SCC = 211