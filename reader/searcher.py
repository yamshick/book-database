import re

def get_list_of_substring_in_book(sub, book):
    try:
        # print(book)
        subs_index_list = [m.start() for m in re.finditer(sub, book)]
        return subs_index_list
    except Exception as e:
        print("get_list_of_substring_in_book error", e)


def get_book_fragments_with_substring(book, sub_string, fragment_left_offset = 50, fragment_right_offset = 50):
    try:
        subs_index_list = get_list_of_substring_in_book(sub_string, book)
        fragments = []
        # print("subs_index_list:", subs_index_list)
        for sub_start in subs_index_list:
            left = max(sub_start - fragment_left_offset, 0)
            right = min(sub_start + fragment_right_offset, len(book))
            fragment = book[left:right]
            # fragment = book.slice(left,right)
            fragments.append(fragment)
        return fragments 
    except Exception as e:
        print("get_book_fragments_with_substring error", e)
