def compressor(file_path):
    frequency = {}

    with open(file_path, "r") as file:
        content = file.read()

    for char in content:
        if char in frequency:
            frequency[char] += 1
        else:            
            frequency[char] = 1

    return frequency

def main():
    file_path = "input.txt"
    frequency = compressor(file_path)

    for char, freq in frequency.items():
        print(f"Character: '{char}' Frequency: {freq}")

main()