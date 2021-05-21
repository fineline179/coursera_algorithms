from graphUtils import *

# test BFS on undir graph
print("Test BFS on undir graph")
undir_edge_list = [(0, 1), (2, 3), (2, 4), (3, 4), (4, 5)]

g = Graph(7)
for edge in undir_edge_list:
  g.addUndirEdge(*edge)

g.printGraphConnections()
# print("\n")

for i in range(7):
  bfs_and_print_attributes(g, i)

# test reversing edges on dir graph
print("\nTest reversing edges on dir graph")
dir_edge_list = [(0, 1), (2, 3), (3, 4), (4, 2), (4, 5)]

gg = Graph(7)
for edge in dir_edge_list:
  gg.addDirEdge(*edge)

print("original")
gg.printGraphConnections()

print("\nreversed")
gg.revEdges()
gg.printGraphConnections()


