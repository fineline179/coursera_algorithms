# graphUtils for Prim's minimum spanning tree assignment

import math


class Graph:
  """ Undirected graph class with edge weights"""

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

  def addUndirEdge(self, u: int, v: int, weight: int = 1):
    # Add weighted undirected edge from node u to v.
    assert u in range(self.n) and v in range(self.n)
    if u != v:  # no circular edges
      self.edges[u].append(v)
      self.weights[u].append(weight)
      self.edges[v].append(u)
      self.weights[v].append(weight)

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


def calcMSTPrim(g: Graph, debug=False):
  """Compute minimum spanning tree of graph g, via Prim's algorithm.

  Non heap-based, O(nm) version

  Args:
    g: graph to process
    debug: whether to print debugging information

  Returns:
    List of triples of form (edge_from, edge_to, edge_weight) which form MST
  """
  V = set(range(g.n))  # all nodes
  X = set()  # processed nodes
  T = []  # MST edges
  X.add(0)  # Can start from any source node. Arb choose node 0

  while X != V:
    v_st, w_st = None, None
    min_edge_cost = math.inf
    for v in X:
      for w, cost in zip(g.edges[v], g.weights[v]):
        if w not in X:  # (v, w) is a crossing edge
          if cost < min_edge_cost:
            min_edge_cost = cost
            v_st, w_st = v, w
    X.add(w_st)
    T.append(tuple([v_st, w_st, min_edge_cost]))

  return T










