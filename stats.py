def get_num_words(book):
    word_list = book.split()
    num_words = len(word_list)
    return num_words

def get_character_count(book):
    char_dict = {}
    for char in book:
        char_dict[char.lower()] = char_dict.get(char.lower(), 0) + 1
    return char_dict

def sort_on(items):
    return items["count"]

def get_sorted_list(dict):
    list = []
    for key in dict:
        i = { "name": key, "count": dict[key]}
        list.append(i)
    list.sort(reverse=True, key=sort_on)
    return list
