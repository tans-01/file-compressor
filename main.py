import heapq
import sys
import compressor
from decoder import decoding
from encoder import encode_file, writng_encoded_file
from compressor import huffman_encoding, generate_code

def main():
    if len(sys.argv) > 3:
        print("Usage: python main.py [compress|decompress] <file_path>")
        return 
    command = sys.argv[1]
    file_path = sys.argv[2]

    if command == "compress":
       frequency = compressor.compressor(file_path)
       root = huffman_encoding(frequency)
       codes = generate_code(root, "")
       encoded = encode_file(file_path, codes)
       writng_encoded_file(encoded, "compressed.bin")
       print("File compressed successfully!")
       print(f"\nEncoded: {encoded}")
       print(len(encoded))

    elif command == "decompress":
        frequency = compressor.compressor(file_path)  # ← need this
        root = huffman_encoding(frequency)  
        decoded = decoding(root, "compressed.bin")
        print(f"\nDecoded: {decoded}")




main()
