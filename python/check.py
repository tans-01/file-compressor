with open(r"C:\Users\91700\Downloads\strawberry.jpg", "rb") as f:
    print("Original first bytes:", list(f.read(10)))

with open("decompressed_strawberry.jpg", "rb") as f:
    print("Decompressed first bytes:", list(f.read(10)))