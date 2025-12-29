import re
from pathlib import Path

def count_words(filepath: str) -> int:
    content = Path(filepath).read_text(encoding="utf-8")
    tokens = re.findall(r"\b\w+\b", content)
    return len(tokens)

def main():
    for fname in ["words.txt", "README.md", "test_punctuation.txt", "test_empty.txt"]:
        total = count_words(fname)
        print(f"{fname}: Total words: {total}")

if __name__ == "__main__":
    main()

# Legacy approach (kept for reference):
# with open("words.txt", "r") as file:
#     content = file.read()
#     words = content.split()
# count = 0
# for word in words:
#     count = count + 1
# print(f"Total words: {count}")
# with open("README.md", "r") as file:
#     content = file.read()
#     words = content.split()
# count = 0
# for word in words:
#     count = count + 1
# print(f"Total words: {count}")