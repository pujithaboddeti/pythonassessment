
with open("example.txt", "r") as file:
    file.seek(10)
    content_from_10 = file.read()
    print("Content from position 10:")
    print(content_from_10)
    file.seek(0)
    first_5_bytes = file.read(5)
    print("\nFirst 5 bytes:")
    print(first_5_bytes)
    file.seek(-5, 2)
    last_5_bytes = file.read(5)
    print("\nLast 5 bytes:")
    print(last_5_bytes)
    current_position = file.tell()
    print("\nCurrent position of the pointer:", current_position)
