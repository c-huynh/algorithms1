"""
The file (kargerMinCut.txt) contains the adjacency list representation of a simple undirected graph.
There are 200 vertices labeled 1 to 200. The first column in the file represents
the vertex label, and the particular row (other entries except the first column)
tells all the vertices that the vertex is adjacent to. So for example, the 6th
row looks like : "6	155	56	52	120 ......". This just means that the vertex with
label 6 is adjacent to (i.e., shares an edge with) the vertices with labels
155, 56, 52, 120, ......, etc

Your task is to code up and run the randomized contraction algorithm for the min
cut problem and use it on the above graph to compute the min cut.
(HINT: Note that you'll have to figure out an implementation of edge contractions.
Initially, you might want to do this naively, creating a new graph from the old
every time there's an edge contraction. But you should also think about more
efficient implementations.)
"""

# solution using union find datastructure to represent node contraction
import random
import math
import time
import copy

class Subset(object):
    def __init__(self, parent):
        self.parent = parent
        self.rank = 0

def find(subsets, i):
    """
    finds root and makes root parent of i
    (path compression)
    """
    if subsets[i].parent != i:
        subsets[i].parent = find(subsets, subsets[i].parent)
    return subsets[i].parent

def union(subsets, x, y):
    x_root = find(subsets, x)
    y_root = find(subsets, y)

    # union by rank (put lower rank element under tree)
    if (subsets[x_root].rank < subsets[y_root].rank):
        subsets[x_root].parent = y_root
    elif (subsets[x_root].rank > subsets[y_root].rank):
        subsets[y_root].parent = x_root
    else:
        subsets[y_root].parent = x_root
        subsets[x_root].rank += 1

def min_cut(nodes, edges):

    # create dict of subsets - at start there are len(nodes) subsets
    # each subset has itself as parent
    subsets = {}
    for node in nodes:
        subsets[node] = Subset(node)

    vertices = len(nodes)
    while vertices > 2:
        edge = random.choice(edges)

        subset1 = find(subsets, edge[0])
        subset2 = find(subsets, edge[1])

        if (subset1 != subset2):
            union(subsets, subset1, subset2)
            vertices -= 1

    # count cut edges between two remaining subsets
    cut_edges = 0
    for edge in edges:
        subset1 = find(subsets, edge[0])
        subset2 = find(subsets, edge[1])
        if (subset1 != subset2):
            cut_edges += 1

    return cut_edges

# graph representation
nodes = []
edges = []

# Load data into adjacency_list
with open("kargerMinCut.txt", "r") as f:

    adjacency_list = []
    for line in f:
        adjacency_list.append(line.split())

# extract nodes from adjacency list
for list in adjacency_list:
    nodes.append(list[0])

# create edges from adjacency list
for list in adjacency_list:
    iter_list = iter(list)
    next(iter_list)
    for node in iter_list:
        edge = sorted((list[0], node))
        if edge not in edges:
            edges.append(edge)

n = len(nodes)
# N = int((n**2)*math.log(n))
N = 1000

results = []
start = time.time()
for i in range(0, N):
    results.append(min_cut(nodes, edges))
    if (i%100 == 0):
        print("finished iteration " + str(i) + "...")
end = time.time()

print("minimum cut = " + str(min(results)))
print("elapsed time = " + str(round((end - start), 2)) + "s")
print("iterations performed = " + str(N))

# asnwer = 17