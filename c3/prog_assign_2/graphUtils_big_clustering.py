# graphUtils for big clustering assignment

import math
from collections import deque, defaultdict

class GraphKV:
  """Undirected graph with nodes labeled by arbitrary key"""

  def __init__(self):
    ## Attributes of graph nodes
    # whether node has been visited
    self.visited = {}
    # leader node for each node
    self.leader = {}

    # adjacency list of outgoing edges
    self.edges = defaultdict(set)

  def addUndirEdge(self, u, v):
    self.edges[u].add(v)
    self.edges[v].add(u)
    self.visited[u] = False
    self.visited[v] = False
    self.leader[u] = None
    self.leader[v] = None

  def resetVisited(self):
    # reset all nodes to non-visited
    for key in self.visited.keys():
      self.visited[key] = False

  def resetLeaders(self):
    # reset each node's leader
    for key in self.leader.keys():
      self.leader[key] = None


def bfs(g: GraphKV, source, leader_label):
  """Breadth first search, starting from source node. Labels found nodes as visited,
  and sets their leader value to the specified leader_label

  Args:
    g: graph to search
    source: source node to start search from
    leader_label: label to put on nodes reachable from source
  """
  queue = deque()
  g.visited[source] = True
  g.leader[source] = leader_label
  queue.append(source)

  while len(queue) > 0:
    from_node = queue.popleft()
    for dest_node in g.edges[from_node]:
      if not g.visited[dest_node]:
        g.visited[dest_node] = True
        g.leader[dest_node] = leader_label
        queue.append(dest_node)
