# merge sort
from random import shuffle


def merge(left: list, right: list, debug=False):
  l_arr, r_arr = left.copy(), right.copy()
  sorted_arr = []
  if debug:
    print(f"l_arr = {l_arr}")
    print(f"r_arr = {r_arr}")
    print(f"sorted_arr = {sorted_arr}")

  # merge left and right results
  if debug:
    print(f"\nSTARTING MERGE..")
  while l_arr and r_arr:  # both arrays still have elements
    if l_arr[0] < r_arr[0]:
      sorted_arr.append(l_arr.pop(0))
    else:  # r_arr[0] < l_arr[0]
      sorted_arr.append(r_arr.pop(0))
    if debug:
      print(f"\nl_arr = {l_arr}")
      print(f"r_arr = {r_arr}")
      print(f"sorted_arr = {sorted_arr}")

  # add rest of elements of whichever array was longer
  if l_arr:
    if debug:
      print(f"\nonly l_arr remains")
      print(f"l_arr = {l_arr}")
      print(f"sorted_arr before extend = {sorted_arr}")
    sorted_arr.extend(l_arr)
    if debug:
      print(f"sorted_arr after extend = {sorted_arr}")
  elif r_arr:
    if debug:
      print(f"\nonly r_arr remains")
      print(f"r_arr = {r_arr}")
      print(f"sorted_arr before extend = {sorted_arr}")
    sorted_arr.extend(r_arr)
    if debug:
      print(f"sorted_arr after extend = {sorted_arr}")

  return sorted_arr


def merge_sort(arr: list, l_ind: int, r_ind: int, debug=False):
  assert r_ind >= 0, "r_ind must be >=0"
  assert l_ind >= 0, "l_ind must be >=0"
  assert r_ind >= l_ind, "r_ind must be >= l_ind"

  sorted_arr = []

  # base case
  if r_ind == l_ind:
    sorted_arr.append(arr[l_ind])
    return sorted_arr

  # recursive call mergesort on left and right halves of input array
  midpoint = (l_ind + r_ind) // 2  # midpoint is right boundary of left subarray
  l_arr = merge_sort(arr, l_ind, midpoint, debug=debug)
  r_arr = merge_sort(arr, midpoint + 1, r_ind, debug=debug)

  # merge left and right halves of input array
  sorted_arr = merge(l_arr, r_arr, debug=debug)

  return sorted_arr


#%%
def test_merge():
  left = [2, 3, 7, 9]
  right = [1, 4, 6, 8, 10, 11]

  res = merge(left, right, debug=True)


test_merge()

#%%
def test_merge_sort(input):
  res = merge_sort(input, 0, len(input) - 1, debug=False)
  return res


# even length input
input1 = [2, 3, 7, 9, 1, 4, 6, 8, 10, 11]
input1_answer = sorted(input1)
# odd length input
input2 = [2, 3, 7, 9, 1, 4, 6, 8, 10]
input2_answer = sorted(input2)
# random permutation of first 10000 integers
input3 = list(range(10000))
shuffle(input3)
input3_answer = sorted(input3)


res1 = test_merge_sort(input1)
print(f"input 1 result: {res1 == input1_answer}")
res2 = test_merge_sort(input2)
print(f"input 2 result: {res2 == input2_answer}")
res3 = test_merge_sort(input3)
print(f"input 3 result: {res3 == input3_answer}")
