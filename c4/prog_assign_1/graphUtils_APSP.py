# graphUtils for all pairs shortest path algo

import math
import numpy as np


class Graph:
  """ Directed graph class with in and out edges, and edge weights."""

  def __init__(self, n: int):
    # number of nodes
    self.n = n

    ## Attributes of graph nodes
    # whether node has been visited
    self.visited = [False] * self.n
    # distance from a source node
    self.dist = [math.inf] * self.n

    # adjacency list of outgoing edges
    self.edges = [[] for _ in range(self.n)]
    # weights for outgoing edges
    self.weights = [[] for _ in range(self.n)]
    # adjacency list of incoming edges
    self.in_edges = [[] for _ in range(self.n)]
    # weights for incoming edges
    self.in_weights = [[] for _ in range(self.n)]

  def addDirEdge(self, u: int, v: int, weight: int = 1):
    # Add weighted directed edge from node u to v.
    assert u in range(self.n) and v in range(self.n)
    if u != v:  # no circular edges
      self.edges[u].append(v)
      self.weights[u].append(weight)

  def createInEdgeData(self):
    # create adjacency lists for ingoing edges and weights
    for i in range(self.n):
      for dest, dest_weight in zip(self.edges[i], self.weights[i]):
        self.in_edges[dest].append(i)
        self.in_weights[dest].append(dest_weight)

  def resetVisited(self):
    # reset all nodes to non-visited
    self.visited = [False] * self.n

  def resetDistance(self):
    # reset all nodes to infinite distance
    self.dist = [math.inf] * self.n

  def printGraphConnections(self):
    """Prints graph connections with weights"""
    for i in range(self.n):
      out_edge_string = ", ".join(
        ["{}({})".format(self.edges[i][j], self.weights[i][j])
         for j in range(len(self.edges[i]))])
      out_string = ("Node {} -> ".format(i) + out_edge_string)
      print(out_string)

  def printGraphAttributes(self):
    print("Graph attributes:")
    for i in range(self.n):
      out_string = "Node {}: ".format(i)
      out_string += "visited = {}".format(self.visited[i])
      out_string += ", dist = {}".format(self.dist[i])
      print(out_string)


def calc_APSP_FW(g: Graph, debug=False):
  """Calculate all pairs shortest paths of graph g via Floyd-Warshall algorithm

  Args:
    g: graph to process
    debug: whether to print debugging information

  Returns:
    n x n array of shortest path matrix, and bool of whether result is valid
    (ie no negative cycles)
  """
  n = g.n
  A = np.zeros((n, n, n + 1))
  # initialize base case in A[:, :, 0]
  for i in range(n):
    for j in range(n):
      if i == j:
        pass
      elif j in g.edges[i]:
        A[i, j, 0] = g.weights[i][g.edges[i].index(j)]
      else:
        A[i, j, 0] = np.inf

  for k in range(1, n + 1):
    if debug:
      print(k)
    for i in range(n):
      for j in range(n):
        A[i, j, k] = min(A[i, j, k - 1], A[i, k - 1, k - 1] + A[k - 1, j, k - 1])

  path_lengths = A[:, :, -1]
  # valid if diagonal of final k slice is all zeros
  result_valid = not np.any(path_lengths.diagonal())

  return path_lengths, result_valid


def calcSP_BF(g: Graph, source: int, debug=False):
  """ Use Bellman-Ford alg to calc shortest path from source node to all connected
  nodes.

  Assumes all nodes are connected to source node.
  TODO: check to see if this assumption is needed. eg in Dijkstra's alg, we needed V to
    exclude nodes not reachable from source node. Do we need to do that here? If so,
    insert a preliminary BFS to label reachable nodes..

  TODO: add early stopping condition

  Args:
    g: graph to process
    source: node to start from
    debug: whether to print debugging information
  """

  # create adjacency list for incoming edges
  # (analyzing these versus outgoing edges speeds up algorithm)
  g.createInEdgeData()

  n = g.n
  A = np.zeros((n + 1, n))  # one extra dim on 0-axis to check for negative cycles
  # init base case in A[0, :]
  for i in range(n):
    if i != source:
      A[0, i] = np.inf

  # TODO: early stopping
  for i in range(1, n + 1):
    if debug:
      print(i)
    for v in range(n):  # for each v in V
      # first option
      opt1 = A[i - 1, v]
      # second option: iterate over all nodes w connected to node v
      opt2_vals = [A[i-1, w] + c_wv for w, c_wv in zip(g.in_edges[v], g.in_weights[v])]
      A[i, v] = np.min([opt1] + opt2_vals)

  # last row is check for neg cycles. second to last is list of shortest paths
  path_lengths = A[-2, :]
  # result is valid (ie no neg cycles) if final two rows of A are equal
  result_valid = np.all(A[-2, :] == A[-1, :])

  return path_lengths, result_valid
















