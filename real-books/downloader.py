import os
import requests, zipfile, io


# def rename_files(folder):
#     try:
#         data = os.path.abspath(folder)
#         for i, f in enumerate(os.listdir(data)):
#             src = os.path.join(data, f)
#             print('rename_files', f, f.decode('cp1251').encode('utf8'))
#             os.rename(src, dst)
#     except Exception as e:
#         print("rename_files error", e)
#         raise e

def download(url, folder):
    try:
        r = requests.get(url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(folder)
    except Exception as e:
        print("download error")
        print(url)
        print(e)
        # print('Error', url)    