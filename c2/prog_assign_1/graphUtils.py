import math
from collections import deque

from numpy import array


class Graph:
  def __init__(self, n):
    # number of nodes
    self.n = n

    ## Attributes of graph nodes

    # whether node has been visited
    self.visited = [False] * self.n

    # distance from a source node
    self.dist = [math.inf] * self.n

    # color of node (see CORMEN)
    #  0: white
    #  1: gray
    #  2: black
    self.color = [0] * self.n

    # finishing time for each node
    self.ft = [math.inf] * self.n

    # leader node (for SCC comp)
    self.leader = [math.inf] * self.n

    # adjacency list of outgoing edges
    self.edges = [[] for _ in range(self.n)]

  def addDirEdge(self, u, v):
    # Add directed edge from node u to v.
    assert u in range(self.n) and v in range(self.n)
    if u != v:  # no circular edges
      self.edges[u].append(v)

  def addUndirEdge(self, u, v):
    # Add undirected edge from node u to v.
    assert u in range(self.n) and v in range(self.n)
    if u != v:  # no circular edges
      self.edges[u].append(v)
      self.edges[v].append(u)

  def revEdges(self):
    # reverse edges of graph
    revEdges = [[] for _ in range(self.n)]
    for i in range(self.n):
      for to in self.edges[i]:
        revEdges[to].append(i)
    self.edges = revEdges

  def resetVisited(self):
    # reset all nodes to non-visited
    self.visited = [False] * self.n

  def resetDistance(self):
    # reset all nodes to infinite distance
    self.dist = [math.inf] * self.n

  def resetColor(self):
    # reset all node colors to 0 (white)
    self.color = [0] * self.n

  def resetFinishingTimes(self):
    # reset all finishing times to infinity
    self.ft = [math.inf] * self.n

  def printGraphConnections(self):
    print("Node connections:")
    for i, out_edge_list in enumerate(self.edges):
      out_edge_list_string = ", ".join([str(el) for el in out_edge_list])
      out_string = "Node {} -> ".format(i) + out_edge_list_string
      print(out_string)

  def printGraphAttributes(self, print_ft=False, print_leader=False):
    print("Graph attributes:")
    for i in range(self.n):
      out_string = "Node {}: ".format(i)
      out_string += "visited = {}".format(self.visited[i])
      out_string += ", dist = {}".format(self.dist[i])
      if print_ft:
        out_string += ", ft = {}".format(self.ft[i])
      if print_leader:
        out_string += ", leader = {}".format(self.leader[i])
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


def bfs_and_print_attributes(g: Graph, source):
  # does bfs and prints resultant node info
  bfs(g, source)
  print("\nBFS on node {}".format(source))
  g.printGraphAttributes()


def dfs_rec(g: Graph, source):
  """Depth-first search (recursive)

  Args:
    g: graph to search
    source: source node to start search from
  """
  g.visited[source] = True
  for dest_node in g.edges[source]:
    if not g.visited[dest_node]:
      dfs_rec(g, dest_node)


def dfs_stack(g: Graph, source):
  """Depth-first search (using stack)

  Args:
    g: graph to search
    source: source node to start search from
  """
  stack = deque()
  stack.append(source)
  while len(stack) > 0:
    v = stack.pop()
    if not g.visited[v]:
      g.visited[v] = True
      for dest_node in g.edges[v]:
        stack.append(dest_node)


def calcSCC(g: Graph, use_stack=False):
  """Calc SCC components of graph g

  Args:
    g: graph to calc components of
    use_stack: use stack instead of recursive DFS
  """

  def dfs_rec_set_ft(g: Graph, source):
    """Depth-first search (recursive) that calculates finishing times"""

    nonlocal t
    g.visited[source] = True
    for dest_node in g.edges[source]:
      if not g.visited[dest_node]:
        dfs_rec_set_ft(g, dest_node)
    t += 1
    g.ft[source] = t

  def dfs_stack_set_ft(g: Graph, source):
    """Depth-first search (using stack w/ node colors) that calcs finishing times"""

    nonlocal t
    stack = deque()
    stack.append(source)
    while len(stack) > 0:
      source_node = stack[-1]  # peek top of stack
      if g.color[source_node]:  # if already seen
        source_node = stack.pop()  # done with this node, pop it from the stack
        if g.color[source_node] == 1:  # if GRAY, finish this node
          t += 1
          g.ft[source_node] = t
          g.color[source_node] = 2  # BLACK, done
      else:  # seen for first time
        g.color[source_node] = 1  # GRAY, discovered
        for dest_node in g.edges[source_node]:
          if not g.color[dest_node]:  # if not seen
            stack.append(dest_node)

  def dfs_rec_set_leader(g: Graph, source, leader):
    """Depth-first search (recursive) that sets leader node"""

    g.visited[source] = True
    g.leader[source] = leader
    for dest_node in g.edges[source]:
      if not g.visited[dest_node]:
        dfs_rec_set_leader(g, dest_node, leader)

  def dfs_stack_set_leader(g: Graph, source, leader):
    """Depth-first search (using stack) that sets leader node"""

    stack = deque()
    stack.append(source)
    while len(stack) > 0:
      source_node = stack.pop()
      if not g.visited[source_node]:
        g.visited[source_node] = True
        g.leader[source_node] = leader
        for dest_node in g.edges[source_node]:
          stack.append(dest_node)

  # set dfs functions to use either recursion or stack algorithm
  dfs_ft = dfs_stack_set_ft if use_stack else dfs_rec_set_ft
  dfs_leader = dfs_stack_set_leader if use_stack else dfs_rec_set_leader

  # 1) reverse graph for 1st DFS pass
  g.revEdges()

  # 2) DFS-loop first pass on reversed graph
  t = -1  # finishing time. will be in range [0, ..., n-1], hence start counter at -1
  for i in reversed(range(g.n)):
    if not g.color[i]:
      dfs_ft(g, i)

  # for debugging
  # g.printGraphAttributes(print_ft=True, print_leader=True)

  # 3) DFS-loop second pass on original graph
  g.revEdges()  # reverse edge back to original graph for second pass
  g.resetVisited()  # reset visited status for second pass
  # make map of finishing times to node indices
  ft_to_node = [0] * g.n
  for i in range(g.n):
    ft_to_node[g.ft[i]] = i
  # loop backwards on node in decreasing order of finishing time
  for i in reversed(range(g.n)):
    if not g.visited[ft_to_node[i]]:
      # leader label equals finishing time of leader node from first DFS pass
      leader_label = i
      dfs_leader(g, ft_to_node[i], leader_label)
