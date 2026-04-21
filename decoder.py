import heapq
import json
from node import Node
from compressor import huffman_encoding

def decoding(file_path):
    with open(file_path, "rb") as file:
        freq = file.readline()
        file_string = freq.decode('utf-8')
        print(f"Raw JSON: {file_string}")
        frequency = json.loads(file_string)
        
        print(f"Type: {type(frequency)}")
        heap = [Node(char, freq) for char, freq in frequency.items()]
        heapq.heapify(heap)
        root = huffman_encoding(heap)
        
        decoded = ""
        
        bit_string = ""
        for byte in file.read():
            bit_string += bin(byte)[2:].zfill(8)
            
        current = root
        for bit in bit_string:
            if bit == "0":
                current = current.left
            else:
                current = current.right
            if current.left is None and current.right is None:
                decoded += current.char
                current = root
    return decoded