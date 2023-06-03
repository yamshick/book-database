import sys
import database
import searcher

def manage():
    db_path = sys.argv[1]
    sub_string = sys.argv[2]
    # db_path = '/media/danchick/7848-BA38/Рассказ.db'
    # db_path = '/home/danchick/librarian/book-database/real-books/Рассказ.db'
    # db_path = '/home/danchick/librarian/book-database/Рассказ.db'
    # sub_string = 'термос'
    # fragment_left_offset = 100
    # fragment_right_offset = 100
    # sub_string = 'а'
    try:
        data = database.select_books_info_by_substring(db_path, sub_string)
        # data = database.search_books_info_by_substring(db_path, sub_string)
        for book_info in data:
            book_text = book_info[5]
            header = book_info[0] + " " + book_info[1]
            # print(len(book_text))
            book_fragments = searcher.get_book_fragments_with_substring(book_text, sub_string)
            # print("book_fragments_len:", len(book_fragments))
            print(header)
            for fragment in book_fragments:
                print(fragment.strip(), "\n")
                # print(len(fragment))
    except Exception as e:
        print(e)
             

manage()            