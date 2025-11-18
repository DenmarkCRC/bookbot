def get_num_words(book):
    word_list = book.split()
    num_words = len(word_list)
    return num_words

def get_character_count(book):
    char_dict = {}
    for char in book:
        char_dict[char.lower()] = char_dict.get(char.lower(), 0) + 1
    return char_dict
