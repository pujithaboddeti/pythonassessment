
with open("example.txt", "r") as file:
    file.seek(2)
    content_from_index = file.read()
    print("Content starting from index 15:")
    print(content_from_index)
