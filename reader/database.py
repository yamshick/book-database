import sqlite3

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
        cursor.execute("""SELECT * FROM books WHERE txt LIKE '%термос%'""")
        # cursor.execute("""SELECT * FROM books WHERE txt LIKE ?""", [proper_sub_string])
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

# select_books_info_by_genre('Cпецслужбы')
