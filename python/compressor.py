import heapq

from node import Node

def compressor(file_path):
    frequency = {}

    with open(file_path, "rb") as file:
        content = file.read()

    for char in content:
        if char in frequency:
            frequency[char] += 1
        else:            
            frequency[char] = 1
    frequency_sorted = [Node(char, freq) for char, freq in frequency.items()]
    heap = frequency_sorted
    heapq.heapify(heap)
    return heap, frequency

def huffman_encoding(heap):
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heapq.heappop(heap)

def generate_code(node, code, code_dict={}):
    if node is None:
        return
    if node.right==None and node.left==None:
        code_dict[node.char] = code
    if node:
        generate_code(node.left, code + "0", code_dict)
        generate_code(node.right, code + "1", code_dict)
    return code_dict


