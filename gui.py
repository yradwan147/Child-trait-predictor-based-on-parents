import PySimpleGUI as sg
from functions import face_gen, prob_calc
from PIL import ImageTk


# def eyes():
#     sheet = Image.open("sprites.png")
#     count = 0
#     for x in range(45):
#         for y in range(12):
#             a = (x + 1) * 640
#             b = (y + 1) * 640
#             icon = sheet.crop((a - 640, b - 640, a, b))  # Problem here
#             icon.save("assets/{}.png".format(count))
#             count += 1
#     # First the window layout in 2 columns


# # eyes()

file_list_column = [

    [
        sg.Radio("", "RADIO1", default=True,
                 enable_events=True, key='smooth1'),
        sg.Image('assets/resized/chin1.png'),
        sg.Radio('', "RADIO1", enable_events=True, key='cleft1'),
        sg.Image('assets/resized/chinc.png'),


    ],

    [
        sg.Text('_'*30)
    ],

    [

        sg.Radio('', "RADIO2", default=True,
                 enable_events=True, key='dimple1'),
        sg.Image('assets/resized/dimple.png'),
        sg.Radio('', "RADIO2", enable_events=True, key='dimplen1'),
        sg.Image('assets/resized/dimplen.png'),

    ],
    [
        sg.Text('_'*30)
    ],

    [

        sg.Radio('', "RADIO3", default=True,
                 enable_events=True, key='duplex1'),
        sg.Image('assets/resized/duplex.png'),
        sg.Radio('', "RADIO3", enable_events=True, key='suplex1'),
        sg.Image('assets/resized/blue.png'),

    ],
    [
        sg.Text('_'*30)
    ],

    [

        sg.Radio('', "RADIO4", default=True,
                 enable_events=True, key='attached1'),
        sg.Image('assets/resized/eara.png'),
        sg.Radio('', "RADIO4", enable_events=True, key='free1'),
        sg.Image('assets/resized/earf.png'),
    ],
    [

        sg.Radio('', "RADIO5", default=True,
                 enable_events=True, key='widow1'),
        sg.Image('assets/resized/widow.png'),
        sg.Radio('', "RADIO5", enable_events=True, key='widown1'),
        sg.Image('assets/resized/widown.png'),
    ],

]

file_list1_column = [

    [
        sg.Radio("", "RADIO6", default=True,
                 enable_events=True, key='smooth2'),
        sg.Image('assets/resized/chin1.png'),
        sg.Radio('', "RADIO6", enable_events=True, key='cleft2'),
        sg.Image('assets/resized/chinc.png'),


    ],

    [
        sg.Text('_'*30)
    ],

    [

        sg.Radio('', "RADIO7", default=True,
                 enable_events=True, key='dimple2'),
        sg.Image('assets/resized/dimple.png'),
        sg.Radio('', "RADIO7", enable_events=True, key='dimplen2'),
        sg.Image('assets/resized/dimplen.png'),

    ],
    [
        sg.Text('_'*30)
    ],

    [

        sg.Radio('', "RADIO8", default=True,
                 enable_events=True, key='duplex2'),
        sg.Image('assets/resized/duplex.png'),
        sg.Radio('', "RADIO8", enable_events=True, key='suplex2'),
        sg.Image('assets/resized/blue.png'),

    ],
    [
        sg.Text('_'*30)
    ],

    [

        sg.Radio('', "RADIO9", default=True,
                 enable_events=True, key='attached2'),
        sg.Image('assets/resized/eara.png'),
        sg.Radio('', "RADIO9", enable_events=True, key='free2'),
        sg.Image('assets/resized/earf.png'),
    ],
    [

        sg.Radio('', "RADIO10", default=True,
                 enable_events=True, key='widow2'),
        sg.Image('assets/resized/widow.png'),
        sg.Radio('', "RADIO10", enable_events=True, key='widown2'),
        sg.Image('assets/resized/widown.png'),
    ],

]


# For now will only show the name of the file that was chosen
# shows =
# print(len(shows))
image_viewer_column = [

    [sg.Button('Submit', key='Submit')],
    [sg.Button('Forward', key='Forward')],
    [sg.Button('Back', key='Back')],
    [sg.Image(data='', enable_events=True, background_color='white',
              key='-IMAGE-', right_click_menu=['UNUSED', 'Exit'])]
]


# ----- Full layout -----

layout = [

    [

        sg.Column(file_list_column),

        sg.VSeperator(),

        sg.Column(file_list1_column),

        sg.VSeperator(),

        sg.Column(image_viewer_column),

    ]

]


window = sg.Window("Image Viewer", layout, finalize=True, resizable=True)

tk_shows = []

# Run the Event Loop
offset = -1
while True:

    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:

        break

    elif event == 'Forward':  # if clicked on the image
        # print('forw', offset)
        offset += 1  # add 1 until the last one
        if (offset >= len(tk_shows)):
            offset = 0
        show = tk_shows[offset]  # get a new image
        window['-IMAGE-'].update(data=show)

    elif event == 'Back':
        # print('back', offset)
        offset -= 1  # add 1 until the last one
        if (offset < 0):
            offset = len(tk_shows)-1
        show = tk_shows[offset]  # get a new image
        window['-IMAGE-'].update(data=show)

    elif event == 'Submit':
        parent1 = []
        parent2 = []
        for key, value in values.items():
            print(key, value)
            if value == True:
                print('here')
                if key[-1] == '1':
                    parent1.append(key[:-1])
                elif key[-1] == '2':
                    parent2.append(key[:-1])
        print(parent1, parent2)
        shows = face_gen(prob_calc(parent1[4], parent2[4]), prob_calc(parent1[3], parent2[3]), prob_calc(
            parent1[2], parent2[2]), prob_calc(parent1[1], parent2[1]), prob_calc(parent1[0], parent2[0]))
        tk_shows = []
        for show in shows:
            tk_shows.append(ImageTk.PhotoImage(image=show))

window.close()
