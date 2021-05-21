# graphUtils for Travelling salesman problem

from collections import OrderedDict
from itertools import combinations
import numpy as np


class Graph:
  """ Undirected graph class with edge weights"""

  def __init__(self, n: int):
    # number of nodes
    self.n = n
    # adjacency list of outgoing edges
    self.edges = [[] for _ in range(self.n)]
    # weights for outgoing edges
    self.weights = [[0] * self.n for _ in range(self.n)]

  def addUndirEdge(self, u: int, v: int, weight: int = 1):
    # Add weighted undirected edge from node u to v.
    assert u in range(self.n) and v in range(self.n)
    if u != v:  # no circular edges
      self.edges[u].append(v)
      self.edges[v].append(u)
    self.weights[u][v] = weight
    self.weights[v][u] = weight

  def printGraphConnections(self):
    """Prints graph connections with weights"""
    for i in range(self.n):
      out_edge_string = ", ".join(
        [
          f"{self.edges[i][j]}({self.weights[i][j]:.1f})"
          for j in range(len(self.edges[i]))
        ]
      )
      out_string = f"Node {i} -> " + out_edge_string
      print(out_string)


def calcTS(g: Graph, debug=False):
  """ Calculate minimum cost travelling salesman tour using dynamic programming alg

  Args:
    g: graph to process
    debug: whether to print debugging information

  Returns:
    minimum cost
  """
  n = g.n

  # get all the subsets S for the first 'array' index
  comb_range = range(1, n)
  s_indices = ["0_"]
  for i in range(1, n):
    print(i)
    c1 = combinations(comb_range, i)
    c2 = ["".join(map(lambda x: str(x) + "_", (0, *el))) for el in c1]
    s_indices.extend(c2)

  # create dynamic programming array
  print(f"initializing array")
  arr = OrderedDict([(ind, np.zeros(n)) for ind in s_indices])

  # init base case
  print(f"initializing base case")
  for s_string in list(arr.keys())[1:]:
    arr[s_string][0] = np.inf

  def s_string_to_list(s_str):
    # split into list of numbers, and remove final "_"
    return list(map(int, s_str.split("_")[:-1]))

  print(f"starting algorithm")
  # for each set S other than {0}
  counter = 0
  s_size = len(arr)
  for s_string in list(arr.keys())[1:]:
    if counter % 1000 == 0:
      print(f"{counter}/{s_size} s_string = {s_string}")
    # for each j \el S, j != 0
    j_list = s_string_to_list(s_string)[1:]
    if debug:
      print(f"j_list = {j_list}")
    for j in j_list:
      # get hash index string of 'S - {j}'
      s_no_j_list = [0] + [el for el in j_list if el is not j]
      if debug:
        print(f"s_no_j_list = {s_no_j_list}")
      s_no_j_index = "".join(map(lambda x: str(x) + "_", s_no_j_list))
      if debug:
        print(f"s_no_j_index: {s_no_j_index}")
      vals = [arr[s_no_j_index][k] + g.weights[k][j] for k in s_no_j_list]
      min_val = np.min(vals)
      arr[s_string][j] = min_val
    counter += 1

  # final step
  last_s_ind = list(arr.keys())[-1]
  last_vals = [arr[last_s_ind][j] + g.weights[j][0] for j in range(1, n)]
  min_cost = np.min(last_vals)

  return min_cost
