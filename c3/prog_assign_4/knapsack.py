#%%
from collections import namedtuple
import numpy as np

Item = namedtuple('Item', ['value', 'weight'])


#%%
def calculate_optimal_knapsack_value(item_list, knap_size,
                                     return_subprob_array: bool = False):
  """Given list of (value, weight) objects and knapsack size, calculate optimal
  knapsack value

  Args:
    item_list: list of Item objects
    knap_size: size of knapsack
    return_subprob_array: whether to return array of subproblem solutions

  Returns:
    optimal knapsack value, and subproblem array if indicated
  """
  n, W = len(item_list), knap_size
  A = np.zeros((n + 1, W + 1))
  for i in range(1, n + 1):
    v_i, w_i = item_list[i - 1].value, item_list[i - 1].weight
    for x in range(W + 1):
      term1 = A[i - 1, x]
      term2 = 0 if x - w_i < 0 else A[i - 1, x - w_i] + v_i
      A[i, x] = max(term1, term2)

  opt_val = A[n, W]
  return (opt_val, A) if return_subprob_array else opt_val


# TODO: speed this up by eliminating copies
def calculate_optimal_knapsack_value_terse(item_list, knap_size, debug: bool = False):
  """Given list of (value, weight) objects and knapsack size, calculate optimal
  knapsack value

  This 'terse' version only keeps two columns of the A subproblem matrix.

  Args:
    item_list: list of Item objects
    knap_size: size of knapsack
    debug: print debug info

  Returns:
    optimal knapsack value
  """
  n, W = len(item_list), knap_size
  A = np.zeros((2, W + 1))
  for i in range(1, n + 1):
    if debug and i % 10 == 0:
      print('{}/{}'.format(i, n))
    A[0, :] = A[1, :]
    v_i, w_i = item_list[i - 1].value, item_list[i - 1].weight
    for x in range(W + 1):
      term1 = A[0, x]
      term2 = 0 if x - w_i < 0 else A[0, x - w_i] + v_i
      A[1, x] = max(term1, term2)

  opt_val = A[1, W]
  return opt_val


# TODO: finish
def calculate_optimal_knapsack_items(item_list, knap_size):
  """Given list of (value, weight) objects and knapsack size, calculate indices of
  items in optimal knapsack

  Args:
    item_list: list of Item objects
    knap_size: size of knapsack

  Returns:
    list of indices of items in input list that comprise optimal knapsack
  """
  A = calculate_optimal_knapsack_value(item_list, knap_size,
                                       return_subprob_array=True)[1]



#%% test data
knap_size_test = 6
# optimal: value = 8, solution indices = [2, 3]
item_list_test = [Item(*el) for el in [(3, 4), (2, 3), (4, 2), (4, 3)]]

opt_val_test, A_test = calculate_optimal_knapsack_value(item_list_test,
                                                        knap_size_test, True)

opt_val_test_terse = calculate_optimal_knapsack_value_terse(item_list_test,
                                                            knap_size_test)


# %% problem 1: main data
with open('/home/fineline/projects/coursera-algorithms/c3/prog_assign_4/'
          'knapsack1.txt', 'r') as f:
  knap_size, num_items = [int(x) for x in f.readline().strip().split(' ')]
  item_list = [Item(*map(int, line.strip().split(' '))) for line in f.readlines()]

opt_val = calculate_optimal_knapsack_value(item_list, knap_size)
opt_val_terse = calculate_optimal_knapsack_value_terse(item_list, knap_size)

# optimum value = 2493893


# %% problem 2: main data
with open('/home/fineline/projects/coursera-algorithms/c3/prog_assign_4/knapsack_big'
          '.txt', 'r') as f:
  knap_size_big, num_items_big = [int(x) for x in f.readline().strip().split(' ')]
  item_list_big = [Item(*map(int, line.strip().split(' '))) for line in f.readlines()]

opt_val_big = calculate_optimal_knapsack_value_terse(item_list_big, knap_size_big,
                                                     debug=True)

# optimum value = 4243395