#app
"""

"""


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

books = pd.read_csv('BX-Books.csv' , encoding='latin-1' , on_bad_lines='skip' , sep=';' , low_memory=False, escapechar='\\')
rating = pd.read_csv('BX-Book-Ratings.csv' , encoding='latin-1' , on_bad_lines='skip' , sep=';')
user = pd.read_csv('BX-Users.csv' , encoding='latin-1' ,  on_bad_lines='skip' , sep=';')

def resize_image(image_path, resize=None): #image_path: "C:User/Image/img.jpg"
    if isinstance(image_path, str):
        img = PIL.Image.open(image_path)
    else:
        try:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(image_path)))
        except Exception as e:
            data_bytes_io = io.BytesIO(image_path)
            img = PIL.Image.open(data_bytes_io)

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height/cur_height, new_width/cur_width)
        img = img.resize((int(cur_width*scale), int(cur_height*scale)), PIL.Image.ANTIALIAS)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()


# ui.Image(key="-PHOTO-",size=(50,50) #after some change
# elif event == "-IMG-": # the"-IMG-" key is in [ui.I(key="IMG",enable_events=True), ui.FileBrowse()]
#         window['-PHOTO-'].update(data=resize_image(value["-IMG-"],resize=(50,50)))
# img_list = []
# for i in range(12):
#     r=random.randint(2, 271380)
#     url = books.loc[[r], 'Image-URL-L'].values[0]
#     pic = requests.get(url)
#     bys = BytesIO(pic.content)
#     img_list.append(bys.getvalue())


class app():
    def __init__(wd):

        # image = random_image()
        # size = (500,500)
        # image = convert_to_bytes(image, size, fill=False)

        infor_layout =  [
            # [sg.Button('+', size=(4,2)), sg.Button('-', size=(4,2)), sg.B('Next', size=(4,2)), sg.T(size, size=(10,1), k='-SIZE-')],
            # [sg.Button(image_data=image, key='-BUTTON IMAGE-')],
            [sg.Text("Information of the book:")],
            {sg.Text(size=(40, 1))}
        ]
        
        thumb_layout =  [
            [sg.Text("Pick a book to view the image")],
            [sg.Text(size=(40, 1), key="-TEXT-")],
            [sg.Image(key="-IMAGE-")],
        ]

        list_text = [
            [sg.Text("User ID:")],
            [sg.Input(size=(25, 1), enable_events=True, key="-IN-"), sg.Button('Go')],
            [sg.Text("Information of the reader here:")],
            [sg.Text(size= (25, 5), key="-UID-")],
            
        ]
        list_img = [
            [sg.Image('avatar.png')],
        ]
        list_list = [
            [sg.Listbox(values=[], enable_events=True, size=(50,20), key="-LIST-")],
        ]
        list_layout = [
            [
                sg.Column(list_text),
                sg.Column(list_img),
            ],
            [
                sg.Column(list_list)
            ]
        ]


        wd.layout = [
            [
                sg.Column(list_layout),
                sg.VSeparator(),
                sg.Column(infor_layout),
                sg.VSeparator(),
                sg.Column(thumb_layout),
            ]
        ]

        wd.window = sg.Window('Window Title', wd.layout)
        #toolbar = make_toolbar()
        # u_loc = user.loc[user['User-ID'] == wd.values("-IN-"), 'Location'].values[0]

    def run(wd):
        while True:             # Event Loop
            wd.event, wd.values = wd.window.read()
            if wd.event in (sg.WIN_CLOSED, 'Exit'):
                break

            if wd.event == 'Go':
                uid = int(wd.values["-IN-"])
                loc = user.loc[user['User-ID'] == uid, 'Location'].values[0]
                age = user.loc[user['User-ID'] == uid, 'Age'].values[0]
                if age == "NULL": age = "Unknown"
                read = rating.loc[rating['User-ID'] == uid, 'ISBN'].values[0]
                # book = books.loc[books['ISBN'] == uid, 'Book-Title'].values[0]
                [sg.popup( loc, age, read)]
                
                # wd.button_go(wd)
                # try:
                #     u_loc = user.loc[user['User-ID'] == uid, 'Location'].values[0]
                #     locate = u_loc
                #     wd.window["-UID-"].update(locate)
                # except:
                #     u_loc =[]
                #     wd.window["-UID-"].update(locate)
        wd.window.close()
    
    def button_go(wd):
        loc = user.loc[user['User-ID'] == wd.values["-IN-"], 'Location'].values[0]
        age = user.loc[user['User-ID'] == wd.values["-IN-"], 'Age'].values[0]
        if age == "NULL": age = "Unknown"
        read = rating.loc[rating['User-ID'] == wd.values["-IN-"], 'ISBN'].values[0]
        book = books.loc[books['ISBN'] == read, 'Book-Title'].values[0]
        [sg.popup(loc, age, book)]
        # wd.window['-UID-'].update(u_loc)


        # event_window, event, values = sg.read_all_windows()
        # if event == sg.WIN_CLOSED or event == 'Exit':
        #     break
        # if event == '+':
        #     size = (size[0]+20, size[1]+20)
        # elif event == '-':
        #     if size[0] > 20:
        #         size = (size[0]-20, size[1]-20)
        # elif event in ('Next', '-BUTTON IMAGE-'):
        #     image = random.choice(img_list)
        # elif event_window == toolbar:
        #     image = event_window[event].ImageData

        # Resize image and update the window
        # image = convert_to_bytes(image, fill=True)
        # window['-IMAGE-'].update(data=image)
        # window['-BUTTON IMAGE-'].update(image_data=image)
        # window['-SIZE-'].update(size)
    

my_app = app()
my_app.run()