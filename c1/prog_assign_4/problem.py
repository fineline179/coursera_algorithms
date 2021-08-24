"""
Min Cut
"""

#%%
from random import choice


with open("./c1/prog_assign_4/kargerMinCut.txt", "r") as f:
  graph = [list(map(int, i.split("\t")[:-1])) for i in f.readlines()]


def create():
  """Returns deep copy of graph"""
  global graph
  return [i.copy() for i in graph]


def mincut(g):
  while len(g) > 2:  # while more than 2 vertices
    c1 = choice(range(len(g)))  # pick first vertex, v1
    # delete v1 from graph (will merge into v2), and get list of v1's outgoing edges
    v_del = g.pop(c1)
    c2 = choice(range(1, len(v_del)))  # pick second vertex, v2
    v1, v2 = v_del[0], v_del[c2]  # indices of two vertices, defining chosen edge
    while v2 in v_del:  # remove v2 from v1 outgoing edges
      v_del.remove(v2)
    for i in range(len(g)):
      if g[i][0] == v2:
        # v1 outgoing edges are now added to v2 outgoing edges
        g[i] += v_del
        # v1 no longer exists, so delete outgoing edges from v2 to v1
        while v1 in g[i]:
          g[i].remove(v1)
      # any vertex with outgoing edge to v1 has it replaced by outgoing edge to v2
      for j in range(len(g[i])):
        g[i][j] = v2 if g[i][j] == v1 else g[i][j]
  return len(g[0]) - 1


#%% Testing
mincut(create())

#%% Problems
# calc mincut large N number of times and return smallest value found
N = 300
cut = []
for i in range(N):
  if i % 10 == 0:
    print(i)
  cut += [mincut(create())]

print("\n")
print(min(cut))

# 17
