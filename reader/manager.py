import database

def manage():
    # db_path = '/media/danchick/7848-BA38/Рассказ.db'
    db_path = '/home/danchick/librarian/book-database/real-books/Рассказ.db'
    # db_path = '/home/danchick/librarian/book-database/Рассказ.db'
    sub_string = 'термос'
    # sub_string = 'а'
    try:
        data = database.select_books_info_by_substring(db_path, sub_string)
        # data = database.search_books_info_by_substring(db_path, sub_string)
        print(len(data))
    except Exception as e:
        print(e)
             

manage()            