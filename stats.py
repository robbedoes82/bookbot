def word_count(string):
    wc = len(string.split())
    return wc

def character_count(string):
    character_count = {}
    for letter in string.lower():
        # letter = letter.lower()
        if letter not in character_count:
            character_count[letter] = 1
        else:
            character_count[letter] += 1
    return character_count    

# sort function to sort on value from dic
def sort_on(items):
    return items["num"]

def sort_character_list(character_dic):
    dic_list = []
    for key, value in character_dic.items():
        dic_list.append({"char": key, "num": value})
        dic_list.sort(reverse=True, key=sort_on)
    return dic_list

