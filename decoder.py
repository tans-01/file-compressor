import heapq
import json
from node import Node
from compressor import huffman_encoding

def decoding(file_path):
    with open(file_path, "rb") as file:
        freq_line = file.readline()
        file_string = freq_line.decode('utf-8')
        data = json.loads(file_string)
        frequency = {int(k): v for k, v in data["frequency"].items()}
        filename = "decompressed_" + data["filename"]
        
        heap = [Node(char, freq) for char, freq in frequency.items()]
        heapq.heapify(heap)
        root = huffman_encoding(heap)
        
        decoded = bytearray()
        
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
                decoded.append(current.char)
                current = root
    with open(filename, "wb") as output_file:
        output_file.write(decoded)
    print(f"decompressed to {filename}")