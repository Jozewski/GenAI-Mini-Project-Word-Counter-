with open("words.txt", "r") as file:
    content = file.read()
    words = content.split()

count = 0
for word in words:
    count = count + 1

print(f"Total words: {count}")