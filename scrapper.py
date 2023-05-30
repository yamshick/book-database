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

        authorTag = soup.find("b", string="Автор:")
        # print(authorTag)
        author = authorTag.parent.find("a").text.strip()
        title = soup.find("b", string="Название:").parent.text.replace("Название:", "").strip()
        genre = soup.find("b", string="Жанр:").parent.find("a").text.strip()
        fb2 = "https:" + soup.find("a", string="Скачать в формате FB2")["href"]
        # doc = soup.find("a", string="Скачать в формате DOC")
        # rtf = soup.find("a", string="Скачать в формате RTF")
        txt = "https:" + soup.find("a", string="Скачать в формате TXT")["href"]
        # html = soup.find("a", string="Скачать в формате HTML")
        # epub = soup.find("a", string="Скачать в формате EPUB")

        # print(author, title, genre, txt, fb2)
        time.sleep(SCRAP_DELAY)
        return {"title": title, "author": author, "genre": genre, "txt": txt, "fb2": fb2}
    except Exception as e:
        print(e)
        return {}