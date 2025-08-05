
import sys
from stats import word_count, character_count, sort_character_list

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # filepath = "books/frankenstein.txt"
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = word_count(text)
    character_dic = character_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for  character in sort_character_list(character_dic):
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    # print(sort_character_list(character_dic))
    print("============= END ===============")

main()

