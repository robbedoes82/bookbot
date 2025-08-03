from stats import word_count, character_count

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text


def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_count(text)
    print(f"{num_words} words found in the document")
    print(character_count(text))

main()

