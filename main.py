import heapq

def compressor(file_path):
    frequency = {}

    with open(file_path, "r") as file:
        content = file.read()

    for char in content:
        if char in frequency:
            frequency[char] += 1
        else:            
            frequency[char] = 1
    frequency_sorted = sorted((char, freq) for char, freq in frequency.items())
    heap = frequency_sorted
    heapq.heapify(heap)
    return heap
def huffman_encoding(heap):
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = (left[0] + right[0], left[1] + right[1], left, right)
        heapq.heappush(heap, merged)

    return heapq.heappop(heap)

def main():
    file_path = "input.txt"
    frequency = compressor(file_path)

    for char, freq in frequency:
        print(f"Character: '{char}' Frequency: {freq}")
    root = huffman_encoding(frequency)
    print(f"\nTree root frequency: {root[1]}")
    with open(file_path, "r") as file:
        content = file.read()
    print(len(content))

main()