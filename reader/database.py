import sqlite3
import searcher

def string_to_binary(string):
    # return HEX(string)
    return ' '.join(format(x, 'b') for x in bytearray(string, 'utf-8'))

def select_books_info_by_substring(db_name, sub_string):
    try:
        sqliteConnection = sqlite3.connect(db_name)
        cursor=sqliteConnection.cursor()
        # cursor.execute(sql)
        # 'SELECT * FROM books WHERE genre=' + genre
        proper_sub_string = "%" + sub_string + "%"
        print([proper_sub_string])

        # cursor.execute("""SELECT * FROM books WHERE txt LIKE '%термос%'""")

        cursor.execute("""SELECT * FROM books WHERE txt LIKE ?""", [proper_sub_string])

        # cursor.execute("""SELECT * FROM books WHERE txt LIKE ?""", ["%" + sub_string + "%"])
        # cursor.execute("SELECT * FROM books WHERE txt LIKE '%yes%'")
        # cursor.execute("SELECT * FROM books WHERE txt LIKE '%%'", [sub_string])
        # cursor.execute("SELECT * FROM books WHERE author LIKE ?", [proper_sub_string])
        # cursor.execute("""SELECT * FROM books WHERE author=?""", ['Абдуллаев Хамидулла'])
        print("Connected to SQLite")
        data = cursor.fetchall()
        # print(data)
        print('selected', len(data), 'items')
        # for item in data:
        #     print(item)
        #     print('\n')
        return data
    except sqlite3.Error as error:
        print("Failed select books from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")


def search_books_info_by_substring(db_name, sub_string):
    try:
        sqliteConnection = sqlite3.connect(db_name)
        cursor=sqliteConnection.cursor()
        cursor.execute("""SELECT * FROM books""")
        print("Connected to SQLite")
        data = cursor.fetchall()
        # print(data)
        print('selected', len(data), 'items')
        match_data = []
        for item in data:
            book_text = item[5]
            print('book length', len(book_text))
            subs_list = searcher.get_list_of_substring_in_book(sub_string, book_text)
            if len(subs_list) > 0:
                match_data.append({"book": book_text, "subs_list": subs_list, "sub_string": sub_string})            
        return match_data
    except sqlite3.Error as error:
        print("Failed select books from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")
