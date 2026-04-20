def compressor(file_path):
    frequency = {}

    with open(file_path, "r") as file:
        content = file.read()

    for char in content:
        if char in frequency:
            frequency[char] += 1
        else:            
            frequency[char] = 1
    frequency_sorted = sorted(frequency.items(), key = lambda x: x[1], reverse=True)
    return frequency_sorted

def main():
    file_path = "input.txt"
    frequency = compressor(file_path)

    for char, freq in frequency:
        print(f"Character: '{char}' Frequency: {freq}")

main()