from stats import get_word_count
from stats import get_character_count
from stats import sort_character_count
import sys
def get_book_text(text):
    with open(text) as f:
        book = f.read()
    return book

def main():
    if len(sys.argv) == 2:
        book = get_book_text(sys.argv[1])
        words = get_word_count(book)
        characters = get_character_count(book)
        sorted = sort_character_count(characters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print(" ----------- Word Count ----------")
        print(f"Found {words} total words")
        print("--------- Character Count -------")
        for char in sorted:
            if char["char"].isalpha() == True:
                print(char["char"]+":",char["num"])
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()