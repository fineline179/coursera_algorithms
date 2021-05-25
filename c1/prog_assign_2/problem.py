#%% Coursera c1 w2 assignment: Array inversions


def merge_inversion(left: list, right: list):
  l_arr, r_arr = left.copy(), right.copy()
  sorted_arr = []
  num_lr_inversions = 0

  # merge left and right results
  while l_arr and r_arr:  # both arrays still have elements
    if l_arr[0] < r_arr[0]:
      sorted_arr.append(l_arr.pop(0))
    else:  # r_arr[0] < l_arr[0]
      sorted_arr.append(r_arr.pop(0))
      num_lr_inversions += len(l_arr)

  # add rest of elements of whichever array was longer
  if l_arr:
    sorted_arr.extend(l_arr)
  elif r_arr:
    sorted_arr.extend(r_arr)

  return sorted_arr, num_lr_inversions


def merge_sort_inversion(arr: list, l_ind: int, r_ind: int):
  assert r_ind >= 0, "r_ind must be >=0"
  assert l_ind >= 0, "l_ind must be >=0"
  assert r_ind >= l_ind, "r_ind must be >= l_ind"

  sorted_arr = []

  # base case. length 1 array. no inversions possible
  if r_ind == l_ind:
    sorted_arr.append(arr[l_ind])
    return sorted_arr, 0

  # recursive call mergesort on left and right halves of input array
  midpoint = (l_ind + r_ind) // 2  # midpoint is right boundary of left subarray
  l_arr, num_l_inversions = merge_sort_inversion(arr, l_ind, midpoint)
  r_arr, num_r_inversions = merge_sort_inversion(arr, midpoint + 1, r_ind)

  # merge left and right halves of input array
  sorted_arr, num_lr_inversions = merge_inversion(l_arr, r_arr)

  # total number of inversions from left, right, and split
  num_inversions = num_l_inversions + num_r_inversions + num_lr_inversions

  return sorted_arr, num_inversions


#%%
def test_merge_inversion(left, right):
  res, n_inversions = merge_inversion(left, right)
  print(n_inversions)


l1, r1 = [1, 3, 5], [2, 4, 6]
l2, r2 = [5, 4, 3], [2, 1, 0]
test_merge_inversion(l1, r1)  # should be 3
test_merge_inversion(l2, r2)  # should be 9

#%%
def test_merge_sort_inversion(input):
  res, n_inversions = merge_sort_inversion(input, 0, len(input) - 1)
  return res, n_inversions


input1 = [1, 0]
input2 = [5, 4, 3, 2, 1, 0]
input3 = [0, 1, 2, 3, 4, 5]

res1, n_inversions1 = test_merge_sort_inversion(input1)
print(n_inversions1)  # should be 1
res2, n_inversions2 = test_merge_sort_inversion(input2)
print(n_inversions2)  # should be 15
res3, n_inversions3 = test_merge_sort_inversion(input3)
print(n_inversions3)  # should be 0


#%%
with open("./c1/prog_assign_2/IntegerArray.txt", "r") as f:
  input_array = [int(line) for line in f.readlines()]

res, n_inversions = merge_sort_inversion(input_array, 0, len(input_array) - 1)
print(n_inversions)

# answer: 2407905288
