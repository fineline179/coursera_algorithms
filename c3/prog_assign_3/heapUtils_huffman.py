from collections.abc import Sequence
from collections import namedtuple

class TreeNode:
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
    self.parent = None


HeapNode = namedtuple('HeapNode', ['key', 'val'])

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
    if l is not None and self.L[l].key < self.L[i].key:
      smallest = l
    else:
      smallest = i
    if r is not None and self.L[r].key < self.L[smallest].key:
      smallest = r
    if smallest != i:
      self.swap(i, smallest)
      self.min_heapify(smallest)

  def insert(self, item: HeapNode):
    """Insert item into heap"""
    self.L.append(item)
    item_ind = len(self.L) - 1
    while (self.parent(item_ind) is not None and
           self.L[self.parent(item_ind)].key > item.key):
      self.swap(item_ind, self.parent(item_ind))
      item_ind = self.parent(item_ind)
