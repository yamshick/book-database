import requests, zipfile, io

def download(url, folder):
    try:
        r = requests.get(url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(folder)
    except Exception as e:
        print("download error", url, e)
        # print('Error', url)    