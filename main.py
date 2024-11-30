def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    return file_contents

def characters():
    with open("books/frankenstein.txt") as f:
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

print("--- Begin report of books/frankenstein.txt ---")
print(f"{len(main().split())} words found in the document\n")
for character in characters():
    if character.isalpha():
        print(f"The '{character}' character was found {characters()[character]} times")
print("--- End report ---")
