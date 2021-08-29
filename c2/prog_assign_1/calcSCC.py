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
with open("./c2/prog_assign_1/SCC.txt", "r") as f:
  # input data: list with one element per input file line. each element is tuple of
  # numbers on line, with one subtracted from each number (for 0-based node indexing)
  dir_edge_list = [
    tuple([int(x) - 1 for x in line.strip().split(" ")]) for line in f.readlines()
  ]


#%%
gg = Graph(875714)
for edge in dir_edge_list:
  gg.addDirEdge(*edge)


#%%
calcSCC(gg, use_stack=True)


#%% count number of elements in each leader group
from collections import defaultdict

scc_sizes_dict = defaultdict(int)
for i in range(gg.n):
  scc_sizes_dict[gg.leader[i]] += 1

scc_sizes_sorted = sorted(
  scc_sizes_dict.items(), key=lambda item: item[1], reverse=True
)

# print top 5 largest leader groups
for i in range(5):
  print(scc_sizes_sorted[i])

## Answer
# (615985, 434821)
# (617402, 968)
# (798410, 459)
# (367066, 313)
# (709990, 211)
