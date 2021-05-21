# %%
from graphUtils_dijkstra import *
import sys


# %% setup and analyze test graph
def run_test(test_edges_and_weights: list, num_nodes: int):
  """

  Args:
    test_edges_and_weights: list of edges and weights
    num_nodes: total number of nodes in graph
  """
  gg = Graph(num_nodes)
  for edge_and_weight in test_edges_and_weights:
    gg.addDirEdge(*edge_and_weight)
  gg.printGraphConnections()

  calcShortestPath(gg, source=2)
  print("")
  gg.printGraphAttributes()


data = [(0, 1, 2), (2, 0, 3), (0, 3, 4), (3, 4, 2), (1, 4, 3)]
run_test(data, num_nodes=5)

# %% load data
with open('/home/fineline/projects/coursera-algorithms/c2/prog_assign_2/dijkstraData'
          '.txt', 'r') as f:
  dir_edge_list, dir_edge_weight_list = [], []
  for line in f.readlines():
    if line.strip() != '':
      line_vals = line.strip().split('\t')
      src_node, dest_vals = int(line_vals[0]) - 1, line_vals[1:]
      dir_edges, dir_weights = [], []  # edges and weights for current source node
      for dest_val in dest_vals:  # handle each dest node and weight
        dest_val_split = dest_val.split(',')
        dest_node, dest_weight = int(dest_val_split[0]) - 1, int(dest_val_split[1])
        dir_edges.append(dest_node)
        dir_weights.append(dest_weight)
      dir_edge_list.append(dir_edges)
      dir_edge_weight_list.append(dir_weights)

# %% Construct graph
gg = Graph(200)
for node_num in range(200):
  dest_nodes, dest_weights = dir_edge_list[node_num], dir_edge_weight_list[node_num]
  assert len(dest_nodes) == len(dest_weights)
  for i in range(len(dest_nodes)):
    gg.addDirEdge(node_num, dest_nodes[i], dest_weights[i])

calcShortestPath(gg, source=0)

# %% answer to question
test_nodes = [i - 1 for i in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]]
answer = [gg.A[i] for i in test_nodes]
print(answer)

