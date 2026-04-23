import json

def encode_file(file_path, codes):
    with open(file_path, "rb") as file:
        content = file.read()
    encoded = ""
    for char in content:
        encoded += codes[char]
    return encoded

def writng_encoded_file(encoded, output_path, frequency):
    print(f"Saving frequency: {frequency}")
    json_freq = json.dumps(frequency)
    json_freq_bytes = json_freq.encode('utf-8')
    encoded = encoded + "0" * ((8 - len(encoded) % 8) % 8)
    with open(output_path, "wb") as file:
        file.write(json_freq_bytes)
        file.write(b'\n')
        for i in range(0, len(encoded), 8):
            byte = encoded[i:i+8]
            file.write(int(byte, 2).to_bytes(1, byteorder='big'))
            