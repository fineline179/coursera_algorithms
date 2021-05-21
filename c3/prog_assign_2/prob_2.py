# %%
from graphUtils_big_clustering import *
from itertools import combinations


# %%
def bin_flip_indices(in_string, indices):
  # flip the bits in the binary string in_string at locations in tuple indices
  in_list = [int(c) for c in in_string]
  for ind in indices:
    in_list[ind] = 1 if in_list[ind] == 0 else 0
  return ''.join(map(str, in_list))


def construct_edge_list(node_set, dec_rep=True, print_debug=False):
  # construct edges between all nodes differing by 1 or 2 bits
  edge_list = []
  node_counter = 0
  for curr_node in node_set:
    curr_node_perms = []
    # add all potential single-element permutations
    for i in range(24):
      curr_node_perms.append(bin_flip_indices(curr_node, (i,)))
    # add all potential double-element permutations
    for dp_ind in combinations(range(24), 2):
      curr_node_perms.append(bin_flip_indices(curr_node, dp_ind))

    # if a single or double element permutation of current node is an existing node,
    # add edge between them
    for perm in curr_node_perms:
      if perm in node_set:
        if dec_rep:
          edge_list.append((int(curr_node, 2), int(perm, 2)))
        else:
          edge_list.append((curr_node, perm))

    if print_debug and node_counter % 100 == 0:
      print('{}/{}'.format(node_counter, len(node_set)))
    node_counter += 1

  return edge_list


def calc_components(g: GraphKV):
  # label components of g via bfs. return number of comps.
  component_label = -1
  g.resetVisited()
  for node in g.leader.keys():
    if not g.visited[node]:
      component_label += 1
      bfs(g, node, component_label)

  return component_label + 1


# %% test data
test_node_list = ['0000 0000 0000 0000 0000 0000', '0000 0000 0000 0000 0000 0001',
                  '1000 0000 0000 0000 0000 0000', '1000 0000 0000 0000 0000 0001',
                  '1000 0000 0000 0000 0000 0011', '1111 1111 1111 1111 1111 1111',
                  '1111 1111 1111 1111 1111 1100']

test_node_set = {el.replace(' ', '') for el in test_node_list}

# construct edges
test_edge_list = construct_edge_list(test_node_set, dec_rep=True)

# create graph
gg_test = GraphKV()
for edge in test_edge_list:
  gg_test.addUndirEdge(*edge)

print('number of components: {}'.format(calc_components(gg_test)))


# %% main data
with open('/home/fineline/projects/coursera-algorithms/c3/prog_assign_2'
          '/clustering_big.txt', 'r') as f:
  num_nodes = int(f.readline().strip().split(' ')[0])
  # note: uses replace to remove spaces from each input line
  node_list = [line.strip().replace(' ', '') for line in f.readlines()]

# remove duplicate nodes
node_set = set(node_list)

# %% construct edges
edge_list = construct_edge_list(node_set, dec_rep=True, print_debug=True)

#%% create graph
gg = GraphKV()
edge_add_counter = 0
for edge in edge_list:
  gg.addUndirEdge(*edge)
  if edge_add_counter % 1000 == 0:
    print(edge_add_counter)
  edge_add_counter += 1

#%%
print('number of components: {}'.format(calc_components(gg)))

# 619 components from added edges
# len(node_set) - len(gg.visited) = 198788 - 193289 = 5499 nodes not added via edges
# 619 + 5499 = 6118 total components
