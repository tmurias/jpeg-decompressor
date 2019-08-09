import binarytree
import numpy as np


class HuffmanNode(binarytree.Node):
    def __init__(self, label, value, left=None, right=None):
        self.label = label
        super(HuffmanNode, self).__init__(value, left, right)

def encode_csv(csv_filename):
    csv_values = genfromtxt(sys.argv[1], delimiter=',')
    freq_counter = dict()
    for val in np.nditer(csv_values):
        if val in freq_counter:
            freq_counter[val] += 1
        else:
            freq_counter[val] = 1
    hnodes = []
    for val, freq in freq_counter.items():
        hnodes.append(HuffmanNode(bytes([val]), freq))
    # TODO: Create binary tree from nodes to determine Huffman codes

def _two_smallest(nodes_list):
    """Returns the indexes of the 2 HuffmanNodes in nodes_list with the smallest values.
    """
    smallest = None
    sec_smallest = None
    for i, hnode in enumerate(nodes_list):
        if smallest is None:
            smallest = i
        elif hnode.value <= nodes_list[smallest].value:
            sec_smallest = smallest
            smallest = i
        elif sec_smallest is None:
            sec_smallest = i
        elif hnode.value < nodes_list[sec_smallest].value:
            sec_smallest = i
    return smallest, sec_smallest


