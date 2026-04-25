import json
import os

def encode_file(file_path, codes):
    with open(file_path, "rb") as file:
        content = file.read()
    print(f"First byte: {content[0]}, type: {type(content[0])}")
    print(f"First code key type: {type(list(codes.keys())[0])}")
    encoded = ""
    for char in content:
        encoded += codes[char]
    return encoded

def writng_encoded_file(encoded, output_path, frequency, file_path):
    
    filename = os.path.basename(file_path)
    padding = (8 - len(encoded) % 8) % 8
    encoded = encoded + "0" * padding
    data = {
        "filename" : filename,
        "frequency": frequency,
        "padding": padding
    }
    json_data = json.dumps(data).encode('utf-8')
    
    with open(output_path, "wb") as file:
        file.write(json_data)
        file.write(b'\n')
        for i in range(0, len(encoded), 8):
            byte = encoded[i:i+8]
            file.write(int(byte, 2).to_bytes(1, byteorder='big'))
            
    print(f"First few bits encoded: {encoded[:32]}")