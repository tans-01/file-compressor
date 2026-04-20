def encode_file(file_path, codes):
    with open(file_path, "r") as file:
        content = file.read()
    encoded = ""
    for char in content:
        encoded += codes[char]
    return encoded

def writng_encoded_file(encoded, output_path):
    encoded = encoded + "0" * ((8 - len(encoded) % 8) % 8)
    with open(output_path, "wb") as file:
        for i in range(0, len(encoded), 8):
            byte = encoded[i:i+8]
            file.write(int(byte, 2).to_bytes(1, byteorder='big'))
            