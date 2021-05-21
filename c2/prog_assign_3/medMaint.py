#%%
from heapUtils import MaxHeap, MinHeap


#%%
def running_median(test_data):
  medians = []  # list of running medians
  heap_low = MaxHeap()
  heap_high = MinHeap()

  first_el = test_data.pop(0)
  # log median (median is sole value by definition)
  medians.append(first_el)

  second_el = test_data.pop(0)
  # put first two elements in separate heaps, so we don't have to deal with None heaps
  if first_el < second_el:
    heap_low.insert(first_el)
    heap_high.insert(second_el)
  else:
    heap_low.insert(second_el)
    heap_high.insert(first_el)
  # log median
  medians.append(heap_low.max())

  # process rest of elements
  while test_data:
    el = test_data.pop(0)
    # insert next element in proper heap
    # NB: this logic assumes no duplicate values, and uses max of heap_low as decision
    #  boundary for which heap to put element in
    if el < heap_low.max():
      heap_low.insert(el)
    else:
      heap_high.insert(el)

    # rebalance if heap sizes differ by more than 1
    if len(heap_low) > len(heap_high) + 1:
      el_to_move = heap_low.extract_max()
      heap_high.insert(el_to_move)
    elif len(heap_high) > len(heap_low) + 1:
      el_to_move = heap_high.extract_min()
      heap_low.insert(el_to_move)

    # handles two cases:
    # 1) heap_low is bigger than heap_high, so odd num elements total, and median is
    #    top of heap_low
    # 2) heap_low is same size as heap_high, so even num elements total, and median is
    #    defined as smaller of middle two values, which is also at top of heap_low
    if len(heap_low) >= len(heap_high):
      median = heap_low.max()
    # if heap_high is bigger than heap_low, then we have odd number of elements,
    #  and top of heap_high is median
    else:
      median = heap_high.min()

    # log median
    medians.append(median)

  return medians


#%% Test data
test_data_odd = [8, 3, 5, 6, 10, 2, 1, 7, 11, 9, 4]
test_data_even = [7, 5, 4, 2, 3, 9, 10, 8, 1, 6]

print(running_median(test_data_even))
print(running_median(test_data_odd))


#%% Import data
with open('/home/fineline/projects/coursera-algorithms/c2/prog_assign_3/Median.txt',
          'r') as f:
  data = [int(line.strip()) for line in f]

medians = running_median(data)
print(sum(medians) % 10000)
