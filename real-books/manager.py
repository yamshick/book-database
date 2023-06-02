# from downloader import download
import os
from scrapper import scrap_book_download_page
import database
import downloader
import converter
import cleaner
# from database import insert_book_description, select_books_info_by_genre


def manage():
    try:
        genre = 'Военная документалистика'
        download_folder = 'raw-files'
        convert_folder = 'utf-8-files'
        books_info = database.select_books_info_by_genre(genre)
        for book_info in books_info:
            title = book_info[0]
            author = book_info[1]
            genre = book_info[2]
            year = book_info[3]
            publisher = book_info[4]
            txt_url = book_info[5]
            downloader.download(txt_url, download_folder)
            file_name = ''
            downloaded_files = os.listdir(os.getcwd() + "/" + download_folder)
            for cur_filename in downloaded_files:
                strip_file_name, file_extension = os.path.splitext(cur_filename)
                # print('file_extension: ', file_extension)
                if file_extension == '.txt':
                    file_name = cur_filename
                    # print('file_name:', file_name, file_extension, cur_filename)
            try:        
                converter.convert_cp1251_to_utf8(download_folder, convert_folder, file_name)
                converted_txt_path = convert_folder + '/' + file_name
                database.insertTxtBook(genre, title, author, genre, year, publisher, converted_txt_path)
                cleaner.clean_folder(download_folder)
                cleaner.clean_folder(convert_folder)
                # print (title, author, genre, year, publisher, txt_url)
                # print('\n')
            except Exception as e:
                print(e)    
            continue

        return
        total = len(book_download_pages)
        left = 0
        right = total - 1
        # pages = book_download_pages
        for i in range(left, right):
            page = book_download_pages[i]
            try:
                https_page = 'https' + page[4:-1]
                page_data = scrap_book_download_page(https_page)
                print(page_data)

                # download(page_data["fb2"])
                # download(page_data["txt"])
                database.insert_book_description(
                    page_data["title"],
                    page_data["author"],
                    page_data["genre"],
                    page_data["year"],
                    page_data["publisher"],
                    page_data["txt"],
                    page_data["fb2"]
                )
                print(left," [", i, "] ", right)
                print("total: ", total)
            except Exception as e:
                print("ERROR: ", page, "\n", e)        
                
    except Exception as e:
        print(e)        
        # download('https://royallib.com/get/txt/bochkov_aleksandr/_mi_sprosim_za_vsyo__pogranichniy_rubeg.zip')


manage()    