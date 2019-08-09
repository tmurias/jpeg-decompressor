import binarytree
import numpy as np


class HuffmanNode(binarytree.Node):
    def __init__(self, label, value, left=None, right=None):
        self.label = label
        super(HuffmanNode, self).__init__(value, left, right)

def encode_csv(csv_filename):
    csv_values = np.genfromtxt(csv_filename, delimiter=',')
    freq_counter = dict()
    print(csv_values.shape)
    for val in csv_values.flat:
        val_int = int(val)
        if val_int in freq_counter:
            freq_counter[val_int] += 1
        else:
            freq_counter[val_int] = 1
    hnodes = []
    for val, freq in freq_counter.items():
        hnodes.append(HuffmanNode(bytes([val]), freq))
    while len(hnodes) > 1:
        i, ii = _two_smallest(hnodes)
        smallest = hnodes[i]
        sec_smallest = hnodes[ii]
        new_label = smallest.label + sec_smallest.label
        new_value = smallest.value + sec_smallest.value
        new_node = HuffmanNode(new_label, new_value)
        new_node.left = smallest
        new_node.right = sec_smallest
        if i > ii:
            hnodes.pop(i)
            hnodes.pop(ii)
        else:
            hnodes.pop(ii)
            hnodes.pop(i)
        hnodes.append(new_node)
    huf_tree = hnodes[0]
    print(huf_tree)
    # TODO: Turn tree into actual values


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


