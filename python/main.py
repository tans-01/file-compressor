import heapq
import os
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
       filename = os.path.basename(file_path)
       file_output = filename + ".bin" 
       print(f"Output file: {file_output}")  # ← add this
       heap, frequency = compressor.compressor(file_path)
       root = huffman_encoding(heap)
       codes = generate_code(root, "")
       encoded = encode_file(file_path, codes)
       writng_encoded_file(encoded, file_output, frequency, file_path)
       print("File compressed successfully!")
       

    elif command == "decompress": 
         decoded = decoding(file_path)
         




main()
