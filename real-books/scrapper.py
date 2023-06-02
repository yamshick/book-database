import requests
import time
from bs4 import BeautifulSoup


# file = open("test.txt", "w")

SCRAP_DELAY = 0.001

def scrap_book_download_page(url):
    try:
        page = requests.get(url)
        # print(url)
        # file.write(page.content.__str__())
        # return
        soup = BeautifulSoup(page.content, "html.parser")

        # print(url)
        # file.write(soup.__str__())

        title = ""
        author = ""
        genre = ""
        year = ""
        publisher = ""
        fb2 = ""
        txt = ""

        try:
            authorTag = soup.find("b", string="Автор:")
            author = authorTag.parent.find("a").text.strip()
        except Exception as e:
            print("AUTHOR ERROR: ", e)

        try:
            title = soup.find("b", string="Название:").parent.text.replace("Название:", "").strip()
        except Exception as e:
            print("TITLE ERROR: ", e)

        try:
            genre = soup.find("b", string="Жанр:").parent.find("a").text.strip()
        except Exception as e:
            print("GENRE ERROR: ", e)

        try:
            publisher = soup.find("b", string="Издательский дом:").parent.text.replace("Издательский дом:", "").strip()
        except Exception as e:
            print("PUBLISHER ERROR: ", e)

        try:
            year = soup.find("b", string="Год издания:").parent.text.replace("Год издания:", "").strip()
        except Exception as e:
            print("YEAR ERROR: ", e)

        try:
            fb2 = "https:" + soup.find("a", string="Скачать в формате FB2")["href"]
        except Exception as e:
            print("FB2 ERROR: ", e)

        try:
            txt = "https:" + soup.find("a", string="Скачать в формате TXT")["href"]
        except Exception as e:
            print("TXT ERROR: ", e)

        # doc = soup.find("a", string="Скачать в формате DOC")
        # rtf = soup.find("a", string="Скачать в формате RTF")
        # html = soup.find("a", string="Скачать в формате HTML")
        # epub = soup.find("a", string="Скачать в формате EPUB")

        # print(author, title, genre, txt, fb2)
        time.sleep(SCRAP_DELAY)
        return {"title": title, "author": author, "genre": genre, "year": year, "publisher": publisher, "txt": txt, "fb2": fb2}
    except Exception as e:
        print(e)
        return {}