"""Module for Huffman encoding the values from a CSV file.
"""
import binarytree
from bitstring import BitArray
import numpy as np


class HuffmanNode(binarytree.Node):
    """Regular Node but with a label in addition to the value.
       The label represents the byte/character being encoded and the value is its frequency.
    """
    def __init__(self, label, value, left=None, right=None):
        self.label = label
        super(HuffmanNode, self).__init__(value, left, right)

def encode_csv(csv_filename):
"""Huffman encode the values in the given CSV file.
    - Read the CSV file
    - Print the dimensions of the data
    - Generate the Huffman tree
    - Print the tree
    - Print what each value will be encoded as
    - Write the encoded bits to a binary file
"""
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
    huf_table = _generate_table(huf_tree)
    encoded_data = BitArray()
    for val in csv_values.flat:
        print('Encoding '+str(val)+' as '+str(huf_table[bytes([int(val)])]))
        encoded_data.append(huf_table[bytes([int(val)])])
    encoded_file = open('encoded', 'wb')
    encoded_data.tofile(encoded_file)
    encoded_file.close()


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


def _generate_table(head):
    table = dict()
    code = BitArray()
    _traverse_tree(head, table, code) 
    return table


def _traverse_tree(node, table, code):
    if node is None:
        return
    elif node.left is None and node.right is None:
        # This is a leaf, add its code to the table
        table[node.label] = code
    else:
        _traverse_tree(node.left, table, code + '0b0')
        _traverse_tree(node.right, table, code + '0b1')
