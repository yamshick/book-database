# # f = open("files/bochkov.txt")
# # text = f.read()
# # print(text)

# with open('files/bochkov.txt', encoding = 'utf-8', mode = 'r') as my_file:
#     text = my_file.read()
#     print(text)

# import chardet
# import pandas as pd

# with open('files/bochkov.txt', 'rb') as f:
#     result = chardet.detect(f.read())  # or readline if the file is large


# data = pd.read_csv('files/bochkov.txt', encoding=result['encoding'], on_bad_lines='skip')
# print(data)

import codecs


def convert_cp1251_to_utf8(input_folder, output_folder, file_name):
    try:
        print('convert_cp1251_to_utf8, file_name', file_name)
        f = codecs.open(input_folder + '/' + file_name, 'r', 'cp1251')
        u = f.read()   # now the contents have been transformed to a Unicode string
        out = codecs.open(output_folder + '/' + file_name, 'w', 'utf-8')
        out.write(u)   # and now the contents have been output as UTF-8
    except Exception as e:
        print("convert_cp1251_to_utf8 error:", e)    