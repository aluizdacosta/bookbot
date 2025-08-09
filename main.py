import sys
from stats import count_words

def main(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    
    return file_contents

def characters(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    
    char_dict = {}

    for character in list(file_contents):
        character = character.lower()
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1

    # Sort dictionary by values in descending order
    sorted_chars = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_chars

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    print(f"--- Begin report of {book_path} ---")
    book_text = main(book_path)
    print(f"{count_words(book_text)} words found in the document\n")
    char_counts = characters(book_path)
    for character in char_counts:
        if character.isalpha():
            print(f"{character}: {char_counts[character]}")
    print("--- End report ---")
