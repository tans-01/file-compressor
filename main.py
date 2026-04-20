import heapq

import compressor
from encoder import encode_file
from compressor import huffman_encoding, generate_code

def main():
    file_path = "input.txt"
    frequency = compressor.compressor(file_path)

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

    encoded = encode_file(file_path, codes)
    print(f"\nEncoded: {encoded}")
    print(len(encoded))

main()