#%% Coursera c4 w4 assignment: 2-SAT
import os
from graphUtils import *

#
def clauses_to_imp_edges(num_vars, clauses):
  """Convert list of clauses to implicative forward and backward expressions

  NB: node indices are still indexed starting at one at this point

  Args:
    clauses: list of clauses

  Returns:
    List of all implicative forward and backward expressions
  """

  forward_imps = [[-el[0], el[1]] for el in clauses]
  for el in forward_imps:
    if el[0] < 0:
      el[0] = -el[0] + num_vars
    if el[1] < 0:
      el[1] = -el[1] + num_vars

  backward_imps = [[-el[1], el[0]] for el in clauses]
  for el in backward_imps:
    if el[0] < 0:
      el[0] = -el[0] + num_vars
    if el[1] < 0:
      el[1] = -el[1] + num_vars

  all_imps = forward_imps + backward_imps

  # go to indices starting at zero, for use in graph class
  all_imps = [[el[0] - 1, el[1] - 1] for el in all_imps]

  return all_imps


def check_sat_of_graph(g: Graph):
  """Checks if SAT-2 conditions in graph are satisfiable"""
  satisfiable = True
  num_vars = int(g.n / 2)
  for i in range(num_vars):  # only need to go through half the graph nodes
    if g.leader[i] == g.leader[i + num_vars]:
      satisfiable = False
      break
  return satisfiable


#%%
def run_test():
  num_vars = 4
  clauses = [[1, 2], [-3, 4], [-2, 3], [-1, 4]]

  all_imps = clauses_to_imp_edges(num_vars, clauses)
  print(all_imps)

  gg = Graph(2 * num_vars)
  for edge in all_imps:
    gg.addDirEdge(*edge)

  calcSCC(gg, use_stack=True)
  satisfied = check_sat_of_graph(gg)
  print(f"satisfiable = {satisfied}")


run_test()

#%%
def load_data(filename):
  file_path = os.path.join("./c4/prog_assign_4", filename)
  with open(file_path, "r") as f:
    num_vars = int(f.readline().strip())
    clauses = [tuple(int(x) for x in line.strip().split(" ")) for line in f.readlines()]

  return num_vars, clauses


def check_sat_of_file(filename):
  num_vars, clauses = load_data(filename)
  all_imps = clauses_to_imp_edges(num_vars, clauses)

  gg = Graph(2 * num_vars)
  for edge in all_imps:
    gg.addDirEdge(*edge)

  calcSCC(gg, use_stack=True)
  satisfied = check_sat_of_graph(gg)
  print(f"{filename}: satisfiable = {satisfied}")


#%%
check_sat_of_file("2sat1.txt")
check_sat_of_file("2sat2.txt")
check_sat_of_file("2sat3.txt")
check_sat_of_file("2sat4.txt")
check_sat_of_file("2sat5.txt")
check_sat_of_file("2sat6.txt")
