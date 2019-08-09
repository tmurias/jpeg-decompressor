import csv_huffman


def test_two_smallest():
    node1 = csv_huffman.HuffmanNode(b'A', 1)
    node2 = csv_huffman.HuffmanNode(b'B', 2)
    node3 = csv_huffman.HuffmanNode(b'C', 3)
    node4 = csv_huffman.HuffmanNode(b'D', 4)
    node5 = csv_huffman.HuffmanNode(b'E', 5)

    failure = False
    if csv_huffman._two_smallest([node1, node2, node3, node4, node5]) != (0, 1):
        failure = True
    if csv_huffman._two_smallest([node5, node4, node3, node2, node1]) != (4, 3):
        failure = True
    if csv_huffman._two_smallest([node4, node3, node1, node2, node4]) != (2, 3):
        failure = True
    if csv_huffman._two_smallest([node1, node2, node3, node5, node4]) != (0, 1):
        failure = True
    if csv_huffman._two_smallest([node3, node2, node1, node4, node5]) != (2, 1):
        failure = True
    if csv_huffman._two_smallest([node2, node1, node3, node4, node5]) != (1, 0):
        failure = True

    if failure:
        print('csv_huffman._two_smallest failed')
    else:
        print('csv_huffman._two_smallest passed')

if __name__ == '__main__':
    test_two_smallest()
