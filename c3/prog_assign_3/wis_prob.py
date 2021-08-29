#%% Coursera c3 w3 assignment, problem 3: maximum-weight independent set

from collections import deque


def calculate_mw(vert_weights: deque, return_mw_recvals: bool = False):
  """ Calculate max weight of max-weight-independent-set (mwis) of input values,
  via iterative dynamic programming method

  Args:
    vert_weights: list of input values of weights of vertices
    return_mw_recvals: whether to return list of max weights of each sublist of
      input values

  Returns:
    max weight of mwis of input values, plus max weights of sublists of input values if
    return_mwis_recvals is set to True.
  """
  A = [0, vert_weights.popleft()]

  while vert_weights:
    w_i = vert_weights.popleft()
    A_i = max(A[-1], A[-2] + w_i)
    A.append(A_i)

  return (A[-1], A) if return_mw_recvals else A[-1]


def calculate_mwis(vert_weights: deque):
  """Calculate max-weight-independent-set (mwis) of input values

  Args:
    vert_weights: list of input values of weights of vertices

  Returns:
    indices of mwis of input values (indices starting at 0)
  """
  A = calculate_mw(vert_weights.copy(), return_mw_recvals=True)[1]

  mwis = []
  i = len(vert_weights)
  while i > 1:
    w_i = vert_weights[i-1]
    if A[i-1] > A[i-2] + w_i:
      i -= 1
    else:
      mwis.append(i-1)
      i -= 2
  if i == 1:
    mwis.append(i-1)

  mwis.reverse()  # reverse list to put in same order as input values
  return mwis


#%% Test data
tests = []
tests.append([1])  # mw 1, mwis = [0]
tests.append([1, 2, 3])  # mw 4, mwis = [0, 2]
tests.append([1, 2, 3, 4])  # mw 6, mwis = [1, 3]
tests.append([4, 1, 6, 5])  # mw 10, mwis = [0, 2]
tests.append([4, 1, 6])  # mw 10, mwis = [0, 2]
tests.append([1, 6, 4])  # mw 6, mwis = [1]

tests = [deque(test) for test in tests]
test_mw_vals = [1, 4, 6, 10, 10, 6]


#%% test mw computation
for t, act_mw in zip(tests, test_mw_vals):
  calc_mw = calculate_mw(t.copy())
  print('data = {}, mw calculated = {}, mw correct = {}, test pass = {}'
        .format(list(t), calc_mw, act_mw, calc_mw == act_mw))


#%% test mwis computation
print('')
test_mwis_vals = [[0], [0, 2], [1, 3], [0, 2], [0, 2], [1]]
for t, act_mwis in zip(tests, test_mwis_vals):
  calc_mwis = calculate_mwis(t.copy())
  print('data = {}, mw calculated = {}, mw correct = {}'
        .format(list(t), calc_mwis, act_mwis))


#%% main data
with open('/home/fineline/projects/coursera-algorithms/c3/prog_assign_3/mwis.txt',
          'r') as f:
  num_vertices = int(f.readline().strip())
  vertex_weights = deque()
  for line in f.readlines():
    vertex_weights.append(int(line.strip()))


#%% calculate answer
mwis = calculate_mwis(vertex_weights)

# subtract one from supplied vertex indices to use 0-based indexing
test_indices = [ind - 1 for ind in [1, 2, 3, 4, 17, 117, 517, 997]]

def is_in(ind):
  return 1 if ind in mwis else 0

answer = [is_in(ind) for ind in test_indices]

# answer = 10100110



