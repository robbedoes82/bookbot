from stats import word_count, character_count, sort_character_list

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text


def main():
    filepath = "books/frankenstein.txt"
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



'''
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============
'''