def encode_file(file_path, codes):
    with open(file_path, "r") as file:
        content = file.read()
    encoded = ""
    for char in content:
        encoded += codes[char]
    return encoded