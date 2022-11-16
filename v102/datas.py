import pandas as pd
from PIL import Image
import requests
from io import BytesIO
from urllib.request import urlopen
import PySimpleGUI as sg
import random
import re
import PySimpleGUI as sg
import PIL
from PIL import Image
import io
import base64
import random
import pandas as pd
import requests
from io import BytesIO
from urllib.request import urlopen
import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen
import cv2
import numpy as np


sg.theme("LightBrown3")
books = pd.read_csv('BX-Books.csv' , encoding='latin-1' , on_bad_lines='skip' , sep=';' , low_memory=False, escapechar='\\')

# x = books.drop(columns=["ISBN"])
# y = books["ISBN"]

rating = pd.read_csv('BX-Book-Ratings.csv' , encoding='latin-1' , on_bad_lines='skip' , sep=';')

# x = rating.drop(columns=["ISBN"])
# y = rating["ISBN"]
# t = rating.drop(columns=["User-ID"])
# r = rating["User-ID"]

user = pd.read_csv('BX-Users.csv' , encoding='latin-1' ,  on_bad_lines='skip' , sep=';')

def find(UID):
    dataset = pd.DataFrame()
    loc = user.loc[user['User-ID'] == int(UID), 'Location'].values[0]
    age = str(user.loc[user['User-ID'] == int(UID), 'Age'].values[0])
    if age == "nan": age = "Unknown"
    read = None
    book = None
    isbn = None
    author = None
    year = None
    publisher = None
    l_url = None
    rate = None
    try:
        read = rating.loc[rating['User-ID'] == int(UID), 'ISBN']
        readd = pd.DataFrame(read)
            # for rowe in readd.iterrows():
            #     print(rowe)
        
        #print(readd)
        if len(read)>=1:
            for rowe in readd.iterrows():
                print(rowe)
                isbn = rowe[1].values[0]
                book = books.loc[books['ISBN'] == isbn, 'Book-Title'].values[0]
                l_url = books.loc[books['ISBN'] == isbn, 'Image-URL-L'].values[0]
                author = books.loc[books['Book-Title'] == book, 'Book-Author'].values[0]
                year = books.loc[books['Book-Title'] == book, 'Year-Of-Publication'].values[0]
                publisher = books.loc[books['Book-Title'] == book, 'Publisher'].values[0]
                isbn = str(books.loc[books['Book-Title'] == book, 'ISBN'].values[0])
                rates = rating.loc[rating['ISBN'] == isbn, 'Book-Rating']
                l=int(len(rates))
                rates = pd.DataFrame(rates)
                if l>=1:
                     total_rate = 0
                     for r in rates.iterrows():
                         total_rate = total_rate + int(r[1].values[0])
                     rate = round(total_rate/l, 1)

                else:
                    rate = 0
                
                data = [UID, loc, age, book, str(isbn), author, str(year), publisher, str(rate), l_url]
                # #print("data:", data)
                datas = pd.DataFrame(data)
                # print(datas)
                # #datas = datas.append([UID, loc, age, book, str(isbn), author, str(year), publisher, str(rate), l_url])
                # dataset.append(datas)
    except:
       pass
    return dataset;

find(3640)





# def find(UID):
#     print("run")
     
#     loc = user.loc[user['User-ID'] == int(UID), 'Location'].values[0]
#     age = str(user.loc[user['User-ID'] == int(UID), 'Age'].values[0])
   
#     if age == "nan": age = "Unknown"
#         # data = [UID, loc, str(age)]
#         # datas = pd.DataFrame(data, columns=['uid', 'loc', 'age'])
#         # dataset.append(datas)
#     try:
#         read = rating.loc[rating['User-ID'] == int(UID), 'ISBN']
#         readd = pd.DataFrame(read)
#         book = None
#         isbn = None
#         author = None
#         year = None
#         publisher = None
#         l_url = None
#         rate = None
                    
    
#         if len(read)>=1:
#                 for row in readd.iterrows():
#                     # print(row[1].values[0])
#                     rate = 0
                

#                     isbn = row[1].values[0]
#                     book = books.loc[books['ISBN'] == isbn, 'Book-Title'].values[0]
#                     l_url = books.loc[books['ISBN'] == isbn, 'Image-URL-L'].values[0]
#                     author = books.loc[books['Book-Title'] == book, 'Book-Author'].values[0]
#                     year = books.loc[books['Book-Title'] == book, 'Year-Of-Publication'].values[0]
#                     publisher = books.loc[books['Book-Title'] == book, 'Publisher'].values[0]
#                     isbn = str(books.loc[books['Book-Title'] == book, 'ISBN'].values[0])
#                     rates = rating.loc[rating['ISBN'] == isbn, 'Book-Rating']
#                     l=int(len(rates))

#                     rates = pd.DataFrame(rates)
#                     if l>=1:
#                         total_rate = 0
#                         for r in rates.iterrows():
#                             total_rate = total_rate + int(r[1].values[0])
#                         rate = round(total_rate/l, 1)

#                     else:
#                         rate = 0

#                     data = [UID, loc, age, book, str(isbn), author, str(year), publisher, str(rate), l_url]
#                     datas = pd.DataFrame(data, columns=['uid', 'loc', 'age', 'book', 'isbn', 'author', 'year', 'publisher', 'rate', 'url'])
#                     # datas = pd.DataFrame(data)
#                     datas.append(datas)
#                 print(datas)
#     except:
#         pass

#     # book = None
#     # isbn = None
#     # author = None
#     # year = None
#     # publisher = None
#     # l_url = None
#     # rate = None
#     # data = [UID, loc, age, book, str(isbn), author, str(year), publisher, str(rate), l_url]
#     # datas = pd.DataFrame(data)
#     # print(datas)
        

   
#     return datas

# print(find('3640'))






# t = user.drop(columns=["User-ID"])
# r = user["User-ID"]

# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


# print(sg.theme[])

# print(books['Image-URL-L'].loc[books['ISBN']=='1853114103', 'last']) #########################
# url = books['Image-URL-L'].loc[books['ISBN']=='1853114103']
# print(url)


#url = books.loc[books['ISBN'] == '1853114103', 'Image-URL-L'].values[0]
# url = str(books.loc[[5], 'Image-URL-L'].values[0])

# # root = tk.Tk()
# u=urlopen(url)
# # raw_data = u.read()
# # u.close()
# # print(np.array(bytearray(u.read())))
# img = cv2.imdecode(np.array(bytearray(u.read())), 1)
# print(img)
# cv2.imshow("name", img)

# photo = ImageTk.PhotoImage(data=raw_data)
# label = tk.Label(image=photo)
# label.image = photo
# label.image = photo
# label.pack()

# root.mainloop()




# pic = requests.get(url)
# bys = BytesIO(pic.content)
# # img_list.append(bys.getvalue())
# bits=bys.getvalue()

# if isinstance(bits, str):
#     img = PIL.Image.open(bits)
# else:
#     try:
#             img = PIL.Image.open(io.BytesIO(base64.b64decode(bits)))
#     except Exception as e:
#             dataBytesIO = io.BytesIO(bits)
#             img = PIL.Image.open(dataBytesIO)

#     # cur_width, cur_height = img.size
#     # if resize:
#     #     new_width, new_height = resize
#     #     scale = min(new_height / cur_height, new_width / cur_width)
#     #     img = img.resize((int(cur_width * scale), int(cur_height * scale)), Image.Resampling.LANCZOS)
#     # if fill:
#     #     if resize is not None:
#     #         img = make_square(img, resize[0])
#     with io.BytesIO() as bio:
#         img.save(bio, format="PNG")
#         del img
# bio.getvalue()

# layout = [
#     [
#         [sg.Image(data=bio.getvalue())],
#     ]
# ]
# window = sg.Window("1", layout)
# while True:
#     event, values = window.read()
#     if event in (sg.WIN_CLOSE, 'Exit'):
#         break





# import requests, imghdr

# # gif_url = 'https://media.tenor.com/images/eff22afc2220e9df92a7aa2f53948f9f/tenor.gif'
# # img_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwXRq7zbWry0MyqWq1Rbq12g_oL-uOoxo4Yw&usqp=CAU'
# for url, save_basename in [
#     # (gif_url, 'gif_download_test'),
#     (img_url, 'img_download_test')
# ]:
#     response = requests.get(url)
#     if response.status_code != 200:
#         raise "URLError"
#     extension = imghdr.what(file=None, h=response.content)
#     save_path = f"{save_basename}.{extension}"
#     with open(save_path, 'wb') as f:
#         f.write(response.content)

# import requests


# filename = url.split('/')[-1]
# r = requests.get(url, allow_redirects=True)
# open(filename, 'wb').write(r.content)
# print(url)
# pic = requests.get(url)
# img = Image.open(BytesIO(pic.content))

# u_loc = user.loc[user['User-ID'] == 12, 'Location'].values[0]
# print(u_loc)
# read = rating.loc[rating['User-ID'] == 3640, ['ISBN']]
# rates = rating.loc[rating['ISBN'] == '3404611306', 'Book-Rating']
# # isbn = books.loc[books['Book-Title'] == name, 'ISBN'].values[0]
# rates = rating.loc[rating['ISBN'] == '3404611306', 'Book-Rating']
# l=int(len(rates))
# total_rate = 0
# rates = pd.DataFrame(rates)
# if l>=1:
#                         for r in rates.iterrows():
#                             total_rate = total_rate + int(r[1].values[0])
#                         rate = total_rate/l
# else:
#                         rate = 0
                    
# print(rate)

# for row in read.iterrows():
#     print(row[1].values[0])

# url_list = []
# for i in range(3):
#     r=random.randint(2, 271380)
#     books = pd.read_csv('BX-Books.csv' , encoding='latin-1' , on_bad_lines='skip' , sep=';' , low_memory=False, escapechar='\\')
#     url = books.loc[[r], 'Image-URL-L'].values[0]
#     url_list.append(url)
# u=random.choice(url_list)
# pic = requests.get(u)
# im=BytesIO(pic.content)
# p=im.getvalue()
# img = Image.open(im)
# print (p)

# def random_image():
#     return random.choice(sg.EMOJI_BASE64_LIST)
# print(random_image)

# in=BytesIO(random_image().content)

#print(img.format, img.size, img.mode)





# import tkinter as tk
# import PySimpleGUI as sg

# #sg.Window(title="Hello World", layout=[[]], margins=(100,50)).read()

# layout = [
#     [
#         sg.Text(books['ISBN'].head(5)),
#         sg.VSeparator(),
#         sg.Text(books['Book-Title'].head(5).values[0]),
#         sg.VSeparator(),
#         sg.Text(books['Book-Author'].head(5).values[0])
#     ],
#     [sg.Button("OK")]
# ]
# window = sg.Window("Demo", layout)
 
# while True:
#     event, values = window.read()
# # End program if user closes window or
# # presses the OK button
#     if event == "OK" or event == sg.WIN_CLOSED:
#         break

# window. close()

#print(books['Book-Author'].where(books['ISBN']==1853114103))
# with pd.option_context('display.max_columns', None):print(books.loc[books['ISBN']=='0312308477'])

# url = "https://python-pillow.org/images/pillow-logo.png"
#img = Image.open(urlopen(url))




#full layout
# layout = [
#     [
#         sg.Image(img),
#         sg.VSeparator(),
#         sg.Button('OK')
       
#     ]
# ]
# window = sg.Window("Mydestiny", layout)
# while True:
#     event, values = window.read()
#     if event == "Exit" or event == sg.WIN_CLOSED:
#         break





# import tensorflow as tf
# model = tf.keras.model.Sequential()

# model.add(tf)