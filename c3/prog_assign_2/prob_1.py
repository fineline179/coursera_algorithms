#%% Coursera c3 w2 assignment, problem 1: K-Clustering

from graphUtils_clustering import *


#%% setup and analyze test graph
def run_test(algo, algo_additional_args=[]):
  edge_weight_list = [(0, 1, 1), (0, 2, 7), (1, 2, 5), (1, 3, 4), (1, 4, 3),
                      (2, 4, 6), (3, 4, 2)]

  print(edge_weight_list)

  gg_mst = algo(5, edge_weight_list, *algo_additional_args)

  print(gg_mst)

# naive and union-find versions of the MST algo should produce same results
run_test(calcMSTKruskal)
print("")
run_test(calcMSTKruskalUF)
print("")
# test k-clustering
run_test(calcMSTKruskalUF, [2])


#%% main data
with open('/home/fineline/projects/coursera-algorithms/c3/prog_assign_2/clustering1'
          '.txt', 'r') as f:
  num_nodes = int(f.readline().strip())
  edge_weight_list = []
  for line in f.readlines():
    data = [int(x) for x in line.strip().split(' ')]
    edge_weight_list.append(tuple([data[0] - 1, data[1] - 1, data[2]]))


#%%
gg_mst = calcMSTKruskalUF(num_nodes, edge_weight_list, k=4)
print("spacing = {}".format(gg_mst[1]))
