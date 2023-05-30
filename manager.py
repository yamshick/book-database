from downloader import download
from scrapper import scrap_book_download_page
# from database import insertBLOB


def manage():
    try:
        book_download_pages = open("books.txt").readlines()
        counter = 1
        pages = book_download_pages[:5]
        for page in pages:
            https_page = 'https' + page[4:-1]
            page_data = scrap_book_download_page(https_page)
            print(page_data)

            download(page_data["fb2"])
            download(page_data["txt"])

            print(counter, "/", len(pages))
            counter +=1
    except Exception as e:
        print(e)        
        # download('https://royallib.com/get/txt/bochkov_aleksandr/_mi_sprosim_za_vsyo__pogranichniy_rubeg.zip')


manage()    