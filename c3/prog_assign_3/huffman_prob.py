#%% Coursera c3 w3 assignment, problems 1 and 2: Huffman Coding

from heapUtils_huffman import *


# %% make min heap of leaf nodes
def create_leafnode_heap(symbol_weight_list):
  symb_heap = MinHeap()

  for sw in symbol_weight_list:
    symb_leaf = TreeNode(sw[0])
    symb_heap.insert(HeapNode(key=sw[1], val=symb_leaf))

  return symb_heap


# make huffman tree
def create_huffman_tree(symb_heap: MinHeap):
  while len(symb_heap) > 2:
    a = symb_heap.extract_min()
    b = symb_heap.extract_min()
    a_b = TreeNode('_'.join([a.val.value, b.val.value]))
    a_b.left, a_b.right = b.val, a.val
    # update parents..
    a_b.left.parent, a_b.right.parent = a_b, a_b
    new_key = a.key + b.key
    symb_heap.insert(HeapNode(key=new_key, val=a_b))

  # root of huffman tree
  a = symb_heap.extract_min()
  b = symb_heap.extract_min()
  huff_tree = TreeNode('_'.join([a.val.value, b.val.value]))
  huff_tree.left, huff_tree.right = b.val, a.val
  huff_tree.left.parent, huff_tree.right.parent = huff_tree, huff_tree

  return huff_tree


# extract encodings from huffman tree
def create_encoding(huff_tree: TreeNode, print_encoding=False):
  code_dict = {}

  def tree_walk(node: TreeNode, code_string, code_dict):
    if node.left is None and node.right is None:
      code_dict[node.value] = code_string
      if print_encoding:
        print('symbol: {}, code: {}'.format(node.value, code_string))
    else:
      tree_walk(node.left, code_string + '0', code_dict)
      tree_walk(node.right, code_string + '1', code_dict)

  tree_walk(huff_tree, '', code_dict)

  return code_dict


#%% test data
test_symbol_weight_list = [('a', 60), ('b', 25), ('c', 10), ('d', 5)]

test_symb_heap = create_leafnode_heap(test_symbol_weight_list)
test_huff_tree = create_huffman_tree(test_symb_heap)
test_code_dict = create_encoding(test_huff_tree)


# %% main data
with open('/home/fineline/projects/coursera-algorithms/c3/prog_assign_3/huffman.txt',
          'r') as f:
  num_symbols = int(f.readline().strip())
  symbol_weight_list = []
  for i, line in enumerate(f.readlines(), start=1):
    symbol_weight_list.append((str(i), int(line.strip())))

symb_heap = create_leafnode_heap(symbol_weight_list)
huff_tree = create_huffman_tree(symb_heap)
code_dict = create_encoding(huff_tree)
code_lengths = [len(value) for (key, value) in code_dict.items()]
print('max code len = {}, min code len = {}'.format(max(code_lengths),
                                                    min(code_lengths)))

# max = 19, min = 9
