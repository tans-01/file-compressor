import heapq


class Node:
    def __init__(self, char, freq):
     self.char = char
     self.freq = freq
     self.left = None
     self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def compressor(file_path):
    frequency = {}

    with open(file_path, "r") as file:
        content = file.read()

    for char in content:
        if char in frequency:
            frequency[char] += 1
        else:            
            frequency[char] = 1
    frequency_sorted = [Node(char, freq) for char, freq in frequency.items()]
    heap = frequency_sorted
    heapq.heapify(heap)
    return heap


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
def main():
    file_path = "input.txt"
    frequency = compressor(file_path)

    for node in frequency:
        print(f"Character: '{node.char}' Frequency: {node.freq}")
    root = huffman_encoding(frequency)
    print(f"\nTree root frequency: {root.freq}")
    with open(file_path, "r") as file:
        content = file.read()
    print(len(content))
    codes = generate_code(root, "")

    for char, code in codes.items():
     print(f"'{char}' : {code}")
main()