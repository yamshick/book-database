import sqlite3

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(title, author, genre, year, publisher, txt_path, fb2_path):
    try:
        sqliteConnection = sqlite3.connect(genre + '.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS books
                  (title TEXT, author TEXT, genre TEXT, year TEXT,
                   publisher TEXT, txt BLOB, fb2 BLOB)
               """)
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO books
                                  (title, author, genre, year, publisher, txt, fb2) VALUES (?, ?, ?, ?, ?, ?, ?)"""

        txt_binary = convertToBinaryData(txt_path)
        fb2_binary = convertToBinaryData(fb2_path)
        # Convert data into tuple format
        data_tuple = (title, author, genre, year, publisher, txt_binary, fb2_binary)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Files inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

# insertBLOB("title", "bochkov", "spec", "2017", "samizdat", "bochkov-utf-8.txt", "files/bochkov.fb2")


def insertTxtBook(title, author, genre, year, publisher, txt_path):
    try:
        sqliteConnection = sqlite3.connect(genre + '.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS books
                  (title TEXT, author TEXT, genre TEXT, year TEXT,
                   publisher TEXT, txt BLOB)
               """)
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO books
                                  (title, author, genre, year, publisher, txt) VALUES (?, ?, ?, ?, ?, ?)"""

        txt_binary = convertToBinaryData(txt_path)
        # Convert data into tuple format
        data_tuple = (title, author, genre, year, publisher, txt_binary)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Book txt inserted succesfully into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert book txt into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")


# insertTxtBook("title", "bochkov", "spec", "2017", "samizdat", "bochkov-utf-8.txt")

def select_books_info_by_genre(genre):
    try:
        sqliteConnection = sqlite3.connect('library.db')
        cursor=sqliteConnection.cursor()
        # cursor.execute(sql)
        # 'SELECT * FROM books WHERE genre=' + genre
        cursor.execute('SELECT * FROM books WHERE genre=?', [genre])
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