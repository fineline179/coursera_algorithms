#%% Coursera c1 w3 assignment: Quicksort
from random import choice


def partition(A, l, r):
  """partition array A between indices l and r. Assumes pivot element is at left of
  array at index l.

  Args:
    A: input list
    l: left index
    r: right index

  Returns:
    Index of pivot location
  """
  p = A[l]
  i = l + 1
  for j in range(l + 1, r + 1):
    if A[j] < p:
      A[i], A[j] = A[j], A[i]
      i += 1
  A[l], A[i - 1] = A[i - 1], A[l]
  return i - 1


def quicksort(A, start, end, pivot_type: str = "random"):

  global c  # for counting comparisons

  if end >= start:
    c += end - start  # increment comparison counter by (length of input - 1)

  if end - start <= 0:  # 1 element sublist
    return

  # choose pivot
  if pivot_type == "first":  # pivot on first element
    p = start
  elif pivot_type == "last":  # pivot on last element
    p = end
  elif pivot_type == "random":  # pivot at random location
    p = choice(range(start, end + 1))
  elif pivot_type == "med":  # pivot from 'median-of-three' pivot rule.
    if end - start == 1:  # input list has length 2
      # for array of length 2, define "middle" element as first element.

      # (NB if we defined it the opposite way -- with the "middle" element as the
      #  second element -- there would still be a single comparison in the partition
      #  call. Therefore this choice doesn't matter for the purpose of counting
      #  quicksort comparisons.)
      p = start
    else:  # input list has length >= 3
      # get values of first, last, and middle elements of input. pivot is element
      # with value in between values of other two.
      med_index = int((start + end) / 2)
      val_ind_pairs = [(A[start], start), (A[med_index], med_index), (A[end], end)]
      p = sorted(val_ind_pairs)[1][1]

  # put pivot element at beginning of array, for passing to partition
  if p != start:
    A[start], A[p] = A[p], A[start]

  pivot_location = partition(A, start, end)

  quicksort(A, start, pivot_location - 1, pivot_type)
  quicksort(A, pivot_location + 1, end, pivot_type)


#%% Testing
def run_test(in_list, pivot_type: str):
  assert pivot_type in ["first", "last", "med", "random"], "invalid pivot type!"
  print(f"input: {in_list}")
  quicksort(in_list, 0, len(in_list) - 1, pivot_type)
  print(f"output: {in_list}")
  print(f"pivot type: {pivot_type}, number of comparisons = {c}")


input0 = [1]
input1 = [2, 1]
input2 = [3, 1, 2]
input3 = [3, 4, 1, 2]
input4 = [1, 5, 2, 3, 4, 8, 6, 9, 10, 7]

c = 0
run_test(input4, "first")


#%% Problem
def solve_problem(pivot_type):
  assert pivot_type in ["first", "last", "med", "random"], "invalid pivot type!"
  with open("./c1/prog_assign_3/QuickSort.txt", "r") as f:
    input_array = [int(line) for line in f.readlines()]
  quicksort(input_array, 0, len(input_array) - 1, pivot_type)
  print(f"pivot type: {pivot_type}, number of comparisons = {c}")


c = 0
solve_problem("first")
c = 0
solve_problem("last")
c = 0
solve_problem("med")

# pivot type: first, number of comparisons = 162085
# pivot type: last, number of comparisons = 164123
# pivot type: med, number of comparisons = 138382
