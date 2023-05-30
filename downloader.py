import requests, zipfile, io

def download(url):
    try:
        r = requests.get(url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(url)
    except Exception as e:
        print("download error", e)
        # print('Error', url)    