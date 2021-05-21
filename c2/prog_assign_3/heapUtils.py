# Heap data structure and tests

from collections.abc import Sequence

class Heap(Sequence):
  def __init__(self):
    self.L = []
    super().__init__()

  def __getitem__(self, i):
    return self.L[i]

  def __len__(self):
    return len(self.L)

  def __repr__(self):
    return str(self.L)

  def left(self, i: int):
    """Index of left child of node at index i"""
    l_val = 2 * i + 1
    return l_val if l_val < len(self.L) else None

  def right(self, i: int):
    """Index of right child of node at index i"""
    r_val = 2 * i + 2
    return r_val if r_val < len(self.L) else None

  def parent(self, i: int):
    """Index of parent of node at index i"""
    return None if i == 0 else (i - 1) // 2

  def swap(self, i: int, j: int):
    temp = self.L[i]
    self.L[i] = self.L[j]
    self.L[j] = temp


class MaxHeap(Heap):
  def __init__(self):
    super().__init__()

  def max(self):
    """Peak max (do not remove)"""
    return self.L[0]

  def extract_max(self):
    """Extract max of heap"""
    if len(self.L) == 0:
      return None
    max_val = self.L[0]
    self.L[0] = self.L[-1]
    self.L.pop()
    self.max_heapify(0)
    return max_val

  def max_heapify(self, i: int):
    """Make subtree at index i a max heap"""
    l, r = self.left(i), self.right(i)
    if l is not None and self.L[l] > self.L[i]:
      largest = l
    else:
      largest = i
    if r is not None and self.L[r] > self.L[largest]:
      largest = r
    if largest != i:
      self.swap(i, largest)
      self.max_heapify(largest)

  def insert(self, item: int):
    """Insert item into heap"""
    self.L.append(item)
    item_ind = len(self.L) - 1
    while self.parent(item_ind) is not None and self.L[self.parent(item_ind)] < item:
      self.swap(item_ind, self.parent(item_ind))
      item_ind = self.parent(item_ind)


class MinHeap(Heap):
  def __init__(self):
    super().__init__()

  def min(self):
    """Peak min (do not remove)"""
    return self.L[0]

  def extract_min(self):
    """Extract min of heap"""
    if len(self.L) == 0:
      return None
    min_val = self.L[0]
    self.L[0] = self.L[-1]
    self.L.pop()
    self.min_heapify(0)
    return min_val

  def min_heapify(self, i: int):
    """Make subtree at index i a min heap"""
    l, r = self.left(i), self.right(i)
    if l is not None and self.L[l] < self.L[i]:
      smallest = l
    else:
      smallest = i
    if r is not None and self.L[r] < self.L[smallest]:
      smallest = r
    if smallest != i:
      self.swap(i, smallest)
      self.min_heapify(smallest)

  def insert(self, item: int):
    """Insert item into heap"""
    self.L.append(item)
    item_ind = len(self.L) - 1
    while self.parent(item_ind) is not None and self.L[self.parent(item_ind)] > item:
      self.swap(item_ind, self.parent(item_ind))
      item_ind = self.parent(item_ind)


# Testing
def main():

  # %% test max heap functionality
  def test_max_heap(data):
    max_heap = MaxHeap()

    for item in data:
      max_heap.insert(item)

    print('')
    print('max heap after construction:')
    print(max_heap)
    print('')

    for _ in range(len(data)):
      print('Max Extaction: {},\t heap: {}'.format(max_heap.extract_max(), max_heap))

  # no duplicates
  max_test_data_1 = [1, 4, 5, 9, 2, 10, 15]
  print('')
  print('-------------------------------------------')
  print('Testing max heap on data without duplicates')
  print('Input: = {}'.format(max_test_data_1))
  test_max_heap(max_test_data_1)

  # with duplicates
  max_test_data_2 = [1, 1, 4, 5, 2, 2, 10]
  print('')
  print('-------------------------------------------')
  print('Testing max heap on data WITH duplicates')
  print('Input: = {}'.format(max_test_data_2))
  test_max_heap(max_test_data_2)

  # %% test min heap functionality
  def test_min_heap(data):
    min_heap = MinHeap()

    for item in data:
      min_heap.insert(item)

    print('')
    print('min heap after construction:')
    print(min_heap)
    print('')

    for _ in range(len(data)):
      print('Min Extaction: {},\t heap: {}'.format(min_heap.extract_min(), min_heap))

  # no duplicates
  min_test_data_1 = [1, 4, 5, 9, 2, 10, 15]
  print('')
  print('-------------------------------------------')
  print('Testing min heap on data without duplicates')
  print('Input: = {}'.format(min_test_data_1))
  test_min_heap(min_test_data_1)

  # with duplicates
  min_test_data_2 = [1, 1, 4, 5, 2, 2, 10]
  print('')
  print('-------------------------------------------')
  print('Testing min heap on data WITH duplicates')
  print('Input: = {}'.format(min_test_data_2))
  test_min_heap(min_test_data_2)


if __name__ == '__main__':
  main()
