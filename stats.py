def get_word_count(book):
    broken_book = book.split()
    num_words = len(broken_book)
    return num_words
def get_character_count(book):
    book = book.lower()
    characters = {}
    for c in book:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters
def sort_on(item):
    return item["num"]
def sort_character_count(dict):
    dict_list = []
    for key, value in dict.items():
        dict_list.append({"char":key, "num":value})
        dict_list.sort(key=sort_on, reverse=True)
    return dict_list

