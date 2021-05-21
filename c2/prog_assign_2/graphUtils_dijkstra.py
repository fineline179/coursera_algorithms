# graphUtils for dijkstra's algorithm assignment

import math
from collections import deque

from numpy import array


class Graph:
  """ Directed graph class with edge weights"""

  def __init__(self, n: int):
    # number of nodes
    self.n = n

    ## Attributes of graph nodes
    # whether node has been visited
    self.visited = [False] * self.n
    # distance from a source node
    self.dist = [math.inf] * self.n
    # shortest path from a source node to each node
    self.A = [1000000] * self.n

    # adjacency list of outgoing edges
    self.edges = [[] for _ in range(self.n)]
    # weights for outgoing edges
    self.weights = [[] for _ in range(self.n)]

  def addDirEdge(self, u: int, v: int, weight: int = 1):
    # Add weighted directed edge from node u to v.
    assert u in range(self.n) and v in range(self.n)
    if u != v:  # no circular edges
      self.edges[u].append(v)
      self.weights[u].append(weight)

  def resetVisited(self):
    # reset all nodes to non-visited
    self.visited = [False] * self.n

  def resetDistance(self):
    # reset all nodes to infinite distance
    self.dist = [math.inf] * self.n

  def resetShortestPath(self):
    # set all shortest paths to default
    self.A = [1000000] * self.n

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
      out_string += ", sp = {}".format(self.A[i])
      print(out_string)


def bfs(g: Graph, source):
  """Breadth first search. Labels found nodes as visited, and sets their distance
  attribute to distance from source node

  Args:
    g: graph to search
    source: source node to start search from
  """
  g.resetVisited()
  g.resetDistance()
  queue = deque()
  g.visited[source] = True
  g.dist[source] = 0
  queue.append(source)

  while len(queue) > 0:
    from_node = queue.popleft()
    for dest_node in g.edges[from_node]:
      if not g.visited[dest_node]:
        g.visited[dest_node] = True
        g.dist[dest_node] = g.dist[from_node] + 1
        queue.append(dest_node)


def calcShortestPath(g: Graph, source: int, debug=False):
  """ Use Dijkstra's alg to calc shortest path from source node to all connected nodes.

  Non heap-based, O(nm) version

  Args:
    g: graph to process
    source: node to start from
    debug: whether to print debugging information
  """

  # Set V equal to all nodes reachable from source node
  bfs(g, source)  # O(n+m)
  V = set([i for i in range(g.n) if g.visited[i]])
  if debug:
    print(V)

  # reset attributes modified by bfs for good form
  g.resetVisited()
  g.resetDistance()

  g.resetShortestPath()
  X = set()  # processed nodes
  X.add(source)
  g.A[source] = 0

  while X != V:
    v_st, w_st = None, None
    min_path_length = math.inf
    for v in X:  # nodes that could be tail of crossing edge
      for w, weight in zip(g.edges[v], g.weights[v]):
        if w not in X:  # (v, w) is a crossing edge
          path_length = g.A[v] + weight
          if path_length < min_path_length:
            min_path_length = path_length
            v_st, w_st = v, w
    X.add(w_st)
    g.A[w_st] = min_path_length













