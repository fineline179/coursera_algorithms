#%% Coursera c4 w1 assignment: All-pairs shortest paths

from graphUtils_APSP import *


#%% analyze test graph using Floyd-Warshall
def run_test_FW():
  # graph in Johnson's algo slides
  edge_weight_list = [
    (0, 1, -2),
    (1, 2, -1),
    (2, 0, 4),
    (2, 3, 2),
    (2, 4, -3),
    (5, 3, 1),
    (5, 4, -4),
  ]

  gg = Graph(6)
  for edge_and_weight in edge_weight_list:
    gg.addDirEdge(*edge_and_weight)

  gg.printGraphConnections()

  shortest_paths, valid_comp = calc_APSP_FW(gg)
  print(shortest_paths)
  print(valid_comp)


run_test_FW()


#%% analyze test graph using Bellman-Ford
def run_test_BF():
  # graph in BF algo slides #3
  edge_weight_list = [(0, 2, 2), (0, 4, 4), (2, 4, 1), (2, 3, 2), (3, 1, 2), (4, 1, 4)]

  # graph with 5 nodes for above data
  ggBF = Graph(5)
  # add graph edges
  for edge_and_weight in edge_weight_list:
    ggBF.addDirEdge(*edge_and_weight)

  ggBF.printGraphConnections()

  shortest_paths, result_valid = calcSP_BF(ggBF, source=0, debug=True)
  print("\n")
  print(shortest_paths)
  print(result_valid)


run_test_BF()


#%% analyze test graph with auxiliary source, using Bellman-Ford. Option for graph
# including a negative cycle
def run_test_BF_aux(neg_cycle=False):
  # graph in Johnson's algo slides
  if not neg_cycle:
    edge_weight_list = [
      (0, 1, -2),
      (1, 2, -1),
      (2, 0, 4),
      (2, 3, 2),
      (2, 4, -3),
      (5, 3, 1),
      (5, 4, -4),
    ]
  else:  # change 1->3 edge from -1 to -3 to make the 0->1->2->0 cycle negative
    edge_weight_list = [
      (0, 1, -2),
      (1, 2, -3),
      (2, 0, 4),
      (2, 3, 2),
      (2, 4, -3),
      (5, 3, 1),
      (5, 4, -4),
    ]

  # graph with 6 nodes for above data, plus extra aux source node
  ggBF = Graph(7)
  # add graph edges
  for edge_and_weight in edge_weight_list:
    ggBF.addDirEdge(*edge_and_weight)

  print("connections before adding aux node:")
  ggBF.printGraphConnections()

  # add aux source node and 0-weighted edges from aux source node to all other nodes
  aux_source_edge_weight_list = [tuple([6, i, 0]) for i in range(6)]
  for aux_source_edge_weight in aux_source_edge_weight_list:
    ggBF.addDirEdge(*aux_source_edge_weight)

  print("\n")
  print("connections after adding aux node:")
  ggBF.printGraphConnections()

  shortest_paths, result_valid = calcSP_BF(ggBF, source=6, debug=True)
  print("\n")
  print(shortest_paths)
  print(result_valid)


run_test_BF_aux(neg_cycle=True)


#%% main data
with open("./c4/prog_assign_1/g3.txt", "r") as f:
  num_nodes, num_edges = tuple([int(x) for x in f.readline().strip().split(" ")])
  edge_weight_list = []
  for line in f.readlines():
    data = [int(x) for x in line.strip().split(" ")]
    edge_weight_list.append(tuple([data[0] - 1, data[1] - 1, data[2]]))


#%% Using Floyd-Warshall
# NB Note sure if my Floyd-Warshall implementation is correct. Gives huge negative
# values in A matrix when run on g1.txt. Haven't tested it on g2.txt and g2.txt yet.
gg = Graph(num_nodes)
for edge_and_weight in edge_weight_list:
  gg.addDirEdge(*edge_and_weight)

shortest_paths, valid_comp = calc_APSP_FW(gg, debug=True)
print(shortest_paths)
print(valid_comp)


#%% Using Bellman-Ford with auxiliary source
ggBF = Graph(num_nodes + 1)
# add graph edges
for edge_and_weight in edge_weight_list:
  ggBF.addDirEdge(*edge_and_weight)

# add aux source node and 0-weighted edges from aux source node to all other nodes
aux_source_edge_weight_list = [tuple([num_nodes, i, 0]) for i in range(num_nodes)]
for aux_source_edge_weight in aux_source_edge_weight_list:
  ggBF.addDirEdge(*aux_source_edge_weight)

shortest_paths, result_valid = calcSP_BF(ggBF, source=num_nodes, debug=True)

print(shortest_paths)
print(result_valid)

# g1.txt has neg cycles
# g2.txt has neg cycles
# shortest path for g3.txt is -19
