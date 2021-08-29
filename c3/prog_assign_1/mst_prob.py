#%% Coursera c3 w1 assignment, problem 3: Minimum Spanning Tree

from graphUtils_mst_prim import *


#%% setup and analyze test graph
def run_test():
  edge_weight_list = [(0, 1, 1), (0, 2, 4), (0, 3, 3), (1, 3, 2), (2, 3, 5)]

  gg = Graph(4)
  for edge_and_weight in edge_weight_list:
    gg.addUndirEdge(*edge_and_weight)

  gg.printGraphConnections()

  gg_mst = calcMSTPrim(gg)

  print(gg_mst)

run_test()


#%% main data
with open('/home/fineline/projects/coursera-algorithms/c3/prog_assign_1/edges.txt',
          'r') as f:
  num_nodes, num_edges = tuple([int(x) for x in f.readline().strip().split(' ')])
  edge_weight_list = []
  for line in f.readlines():
    data = [int(x) for x in line.strip().split(' ')]
    edge_weight_list.append(tuple([data[0] - 1, data[1] - 1, data[2]]))


#%%
gg = Graph(num_nodes)
for edge_and_weight in edge_weight_list:
  gg.addUndirEdge(*edge_and_weight)

gg_mst = calcMSTPrim(gg)


#%%
gg_mst_cost = sum([ew[2] for ew in gg_mst])
