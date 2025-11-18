from stats import get_num_words, get_character_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    char_count = get_character_count(book_text)
    print(f"Found {num_words} total words")
    print(char_count)

main()
