import re

def get_list_of_substring_in_book(sub, book):
    try:
        print(book)
        subs_index_list = [m.start() for m in re.finditer(sub, book)]
        return subs_index_list
    except Exception as e:
        print("get_list_of_substring_in_book error", e)   