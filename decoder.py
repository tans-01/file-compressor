

def decoding(root, file_path):
    with open(file_path, "rb") as file:
        bin_string = ""
        for byte in file.read():
            bin_string += bin(byte)[2:].zfill(8)
        print(bin_string)
    decoded = ""
    current = root
    for bit in bin_string:
        if bit == "0":
            current = current.left
        else:
            current = current.right
        if current.left is None and current.right is None:
            decoded += current.char
            current = root
    return decoded