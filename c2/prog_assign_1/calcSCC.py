#%% Coursera c2 w1 assignment: Strongly connected components of directed graph
from graphUtils import *


#%% setup and analyze test graph
def run_test():
  dir_edge_list = [
    (0, 3),
    (3, 6),
    (6, 0),
    (8, 6),
    (8, 2),
    (2, 5),
    (5, 8),
    (7, 5),
    (1, 7),
    (4, 1),
    (7, 4),
  ]

  gg = Graph(9)
  for edge in dir_edge_list:
    gg.addDirEdge(*edge)

  gg.printGraphConnections()

  calcSCC(gg, use_stack=True)

  print(" ")
  gg.printGraphAttributes(print_ft=True, print_leader=True)


run_test()


#%% main data
with open(
  "/home/fineline/projects/coursera-algorithms/c2/prog_assign_1/SCC.txt", "r"
) as f:
  dir_edge_list = []
  for line in f.readlines():
    if line.strip() != "":
      # subtract one from values to make nodes index from 0
      dir_edge_list.append(tuple([int(x) - 1 for x in line.strip().split(" ")]))


#%%
gg = Graph(875714)
for edge in dir_edge_list:
  gg.addDirEdge(*edge)


#%%
calcSCC(gg, use_stack=True)

#%% count number of elements in each leader group
scc_sizes_dict = {}
for i in range(gg.n):
  if gg.leader[i] not in scc_sizes_dict:
    scc_sizes_dict[gg.leader[i]] = 1
  else:
    scc_sizes_dict[gg.leader[i]] += 1

scc_sizes_sorted = sorted(
  scc_sizes_dict.items(), key=lambda item: item[1], reverse=True
)

# print top 5 largest leader groups
for i in range(5):
  print(scc_sizes_sorted[i])
