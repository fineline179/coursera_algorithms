# Coursera c4 w2 assignment: Traveling salesman

#%%
from graphUtils_TS import *

#%%
def run_test():
  edge_weight_list = [(0, 1, 1), (0, 2, 2), (0, 3, 1), (1, 2, 1), (1, 3, 3), (2, 3, 1)]

  gg = Graph(4)
  for edge_and_weight in edge_weight_list:
    gg.addUndirEdge(*edge_and_weight)

  gg.printGraphConnections()

  min_cost = calcTS(gg)
  print(min_cost)


run_test()

#%%
with open("./c4/prog_assign_2/tsp.txt", "r") as f:
  num_nodes = int(f.readline().strip())
  vertex_coords = [
    tuple(float(x) for x in line.strip().split(" ")) for line in f.readlines()
  ]

# compute edges and weights from node coordinates
edge_weight_list = []
for i, c1 in enumerate(vertex_coords):
  for j, c2 in enumerate(vertex_coords):
    if j > i:
      dist = np.sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2)
      edge_weight_list.append(tuple([i, j, dist]))


gg = Graph(num_nodes)
for edge_and_weight in edge_weight_list:
  gg.addUndirEdge(*edge_and_weight)

min_cost = calcTS(gg, debug=False)

# min_cost = 26442.73030895475
