# Coursera c4 w3 assignment: Travelling salesman revisited

#%%
import numpy as np


def sq_dist(n1, n2, vc):
  """squared distance between two nodes

  Args:
    n1: node 1 index
    n2: node 2 index
    vc: list of vertex coords

  Returns:
    squared dist between nodes
  """
  return (vc[n2][0] - vc[n1][0]) ** 2 + (vc[n2][1] - vc[n1][1]) ** 2


def calc_tour(vertex_coords, print_progress=False):
  remaining_nodes = set(list(range(len(vertex_coords)))[1:])
  num_nodes = len(remaining_nodes)

  tour_order = [0]
  accumulated_distance = 0
  progress_counter = 0
  while remaining_nodes:
    if print_progress and progress_counter % 100 == 0:
      print(f"{progress_counter}/{num_nodes}")
    # calc (node_index, sq_dist) pairs to all other nodes from last node
    dists_to_other_nodes = [
      (n2, sq_dist(tour_order[-1], n2, vertex_coords)) for n2 in remaining_nodes
    ]
    # find index of and squared distance to node nearest to last node
    min_distsq = np.inf
    min_index = 0
    for el in dists_to_other_nodes:
      if el[1] < min_distsq:
        min_distsq = el[1]
        min_index = el[0]
    # add distance to nearest node to tour total, and index of nearest node to tour
    # order
    accumulated_distance += np.sqrt(min_distsq)
    tour_order.append(min_index)
    remaining_nodes.remove(min_index)

    progress_counter += 1

  # add distance back to starting node
  accumulated_distance += np.sqrt(sq_dist(tour_order[-1], 0, vertex_coords))
  # add return to start to end of tour
  tour_order.append(0)

  return tour_order, accumulated_distance


#%%
def run_test(print_tour=False):
  vertex_coords = [(1, 1), (2, 4), (3, 3), (5, 2)]

  tour_order, tour_distance = calc_tour(vertex_coords)
  print(f"Tour distance = {tour_distance}")
  if print_tour:
    print(f"Tour order = {tour_order}")

  # Compare above with:
  #  1) manually calculated shortest tour distance of above tour,
  #  2) manually calculated shortest tour distance of true tour

  def sd(n1, n2):
    """distance between nodes n1 and n2"""
    return np.sqrt(sq_dist(n1, n2, vertex_coords))

  # result of above algorithm, calculated manually
  test_alg = sd(0, 2) + sd(2, 1) + sd(1, 3) + sd(3, 0)
  print(f"raw alg dist = {test_alg}")

  # true shortest tour, calculated manually
  test_true = sd(0, 1) + sd(1, 2) + sd(2, 3) + sd(3, 0)
  print(f"true shortest dist = {test_true}")


run_test(print_tour=True)

#%%
with open("./c4/prog_assign_3/nn.txt", "r") as f:
  num_nodes = int(f.readline().strip())
  vertex_coords = [
    tuple(float(x) for x in line.strip().split(" ")[1:]) for line in f.readlines()
  ]

#%%
tour_order, tour_distance = calc_tour(vertex_coords, print_progress=True)
print(f"Tour distance = {tour_distance}")

# tour distance = 1203406.5012708856
