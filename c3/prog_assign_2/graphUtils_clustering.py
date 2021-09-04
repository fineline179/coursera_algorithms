# graphUtils for clustering assignment

import math
from collections import deque


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
    # leader node for each node
    self.leader = [None] * self.n

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

  def setLeadersToSelf(self):
    # set each node's leader to itself
    self.leader = [i for i in range(self.n)]

  def printGraphConnections(self):
    """Prints graph connections with weights"""
    for i in range(self.n):
      out_edge_string = ", ".join(
        [f"{e}({w})" for e, w in zip(self.edges[i], self.weights[i])]
      )
      out_string = f"Node {i} -> " + out_edge_string
      print(out_string)

  def printGraphAttributes(self):
    print("Graph attributes:")
    for i in range(self.n):
      out_string = f"Node {i}: visited = {self.visited[i]}, dist = {self.dist[i]}"
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


def calcMSTKruskal(num_nodes: int, ew_list: list, debug=False):
  """Compute minimum spanning tree of graph via Kruskal algorithm. Graph defined by
  edge/weight list

  Non union-find vesion, O(nm)

  Args:
    num_nodes: number of nodes in graph
    ew_list: list of weighted edges of form (node1, node2, edge_weight)
    debug: whether to print debugging information

  Returns:
    List of weighted edges (node1, node2, edge_weight) which form MST
  """
  ew_list.sort(key=lambda x: x[2])  # sort edges increasing by weight

  T = []  # current MST edges and weights
  g_mst = Graph(num_nodes)  # graph of current MST

  for ew in ew_list:
    if len(T) == num_nodes - 1:  # stop after adding n-1 edges (MST is complete)
      break
    bfs(g_mst, ew[0])
    # if nodes connected by potential new edge are not yet connected, then union of T
    # and new edge will will not have a cycle
    if not g_mst.visited[ew[1]]:
      g_mst.addUndirEdge(*ew)
      T.append(ew)

  # reset attributes modified by final bfs for good form
  g_mst.resetVisited()
  g_mst.resetDistance()

  return T

def calcMSTKruskalUF(num_nodes: int, ew_list: list, k=1, debug=False):
  """Compute MST or k-clustering of graph via Kruskal algorithm. Graph defined by
  edge/weight list.

  Union-find version, O(m log n)

  Args:
    num_nodes: number of nodes in graph
    ew_list: list of weighted edges of form (node1, node2, edge_weight)
    k: number of clusters. If equal to 1, an MST (1-cluster) is computed
    debug: whether to print debugging information

  Returns:
    List of weighted edges (node1, node2, edge_weight) which form MST or k-clustering,
    and spacing of k-clustering if k > 1.
  """
  assert (k >= 1), "Num clusters k must be greater than 0"

  ew_list.sort(key=lambda x: x[2])  # sort edges increasing by weight

  T = []  # current MST edges and weights
  g_mst = Graph(num_nodes)  # graph of current MST
  g_mst.setLeadersToSelf()

  # Union-Find structure. 'Key' is value of leader node. 'Value' is list of nodes in
  # that leader's component.
  uf_dict = {i: [i] for i in range(num_nodes)}

  for i, ew in enumerate(ew_list):
    if len(T) == num_nodes - k:  # MST or clustering complete
      if k == 1:  # return MST
        return T
      else:  # get spacing of completed k-clustering
        for spacing_ew in ew_list[i:]:  # find next edge that doesn't complete cycle
          if g_mst.leader[spacing_ew[0]] != g_mst.leader[spacing_ew[1]]:
            return T, spacing_ew[2]

    c1, c2 = g_mst.leader[ew[0]], g_mst.leader[ew[1]]
    # if new edge doesn't complete cycle, endpoints in different components
    if c1 != c2:
      # get larger/smaller components
      l_comp, s_comp = ((c1, c2) if len(uf_dict[c1]) > len(uf_dict[c2]) else (c2, c1))
      # update leader nodes of smaller component nodes to leader of larger component
      for s_comp_node in uf_dict[s_comp]:
        g_mst.leader[s_comp_node] = l_comp
      # update UF dict
      uf_dict[l_comp] += uf_dict[s_comp]
      uf_dict[s_comp] = []

      # add edge to graph and MST
      g_mst.addUndirEdge(*ew)
      T.append(ew)
