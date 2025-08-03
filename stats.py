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

# test
# print(character_count("Hallo ik ben Robin, ik ben 42 jaar oud."))