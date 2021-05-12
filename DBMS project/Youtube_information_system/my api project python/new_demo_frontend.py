# Frontend
from tkinter import *
import tkinter.messagebox
import urllib.request
import youtube_api_backend
import json
from tkinter import ttk
import apiclient.discovery


api_key = "AIzaSyDWqzxzO8e_ISSU0vQwfPCs1GzFyTTSB5c"

class Student:

    def __init__(self, root):     #constructor
        self.root = root
        self.root.title("You Tube Information System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")

        You_tube_url = StringVar()

        """ key = "AIzaSyDWqzxzO8e_ISSU0vQwfPCs1GzFyTTSB5c"
        my_list = []
        youtube = apiclient.discovery.build('youtube', 'v3', developerKey=key)
        req = youtube.search().list(part='snippet', q=You_tube_url, maxResults=50, type='channel').execute()
        req = youtube.search().list(part='snippet', q='python programming', maxResults=50, type='channel').execute()
        for item in req['items']:
            my_list.append(item['snippet']['title'])
        clicked = StringVar()
        clicked.set(my_list[0])"""

        # ====================================Functions===============================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("You Tube Information System", "confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtYou_tube_url.delete(0, END)

        def addData():
           # if len(You_tube_url.get()) != 0:
                # query//sort vali fir name ko do
                name = You_tube_url.get()
                data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + str(name) + "&key=" + api_key).read()

                SUBSCRIBER_COUNT = "SUBSCRIBER_COUNT : " + str(json.loads(data)['items'][0]["statistics"]["subscriberCount"])
                VIEW_COUNT = "  VIEW_COUNT : " +  str(json.loads(data)['items'][0]["statistics"]["viewCount"])
                VIDEO_COUNT = "  VIDEO_COUNT : " +  str(json.loads(data)['items'][0]["statistics"]["videoCount"])
                COMMENT_COUNT = "  COMMENT_COUNT : " + str(json.loads(data)['items'][0]["statistics"]["commentCount"])
                HIDDEN_SUBSCRIBER_COUNT = "  HIDDEN_SUBSCRIBER_COUNT : " + str(json.loads(data)['items'][0]["statistics"]["hiddenSubscriberCount"])
                YOU_ID = "  Channel ID : " + str(name)
                youtube_api_backend.youtube_data()
                youtube_api_backend.addytdRec(YOU_ID, VIEW_COUNT, COMMENT_COUNT, SUBSCRIBER_COUNT, HIDDEN_SUBSCRIBER_COUNT, VIDEO_COUNT)
                youtubelist.delete(0, END)
                youtubelist.insert(END, (YOU_ID, VIEW_COUNT, COMMENT_COUNT, SUBSCRIBER_COUNT, HIDDEN_SUBSCRIBER_COUNT, VIDEO_COUNT))

        def DisplayData():
            youtubelist.delete(0, END)
            for row in youtube_api_backend.viewData():
                youtubelist.insert(END, row, str(""))

        def youtubeRec(event):
            global sd
            searchYtd = youtubelist.curselection()[0]
            sd = youtubelist.get(searchYtd)
            self.txtYou_tube_url.delete(0, END)
            self.txtYou_tube_url.insert(END, sd[1])

        def DeleteData():
            if len(You_tube_url.get()) != 0:
                youtube_api_backend.deleteRec(sd[0])
                clearData()
                DisplayData()

        def SearchDatabase():
            youtubelist.delete(0, END)
            for row in youtube_api_backend.searchData(YOU_ID, VIEW_COUNT, COMMENT_COUNT, SUBSCRIBER_COUNT,
                                                      HIDDEN_SUBSCRIBER_COUNT, VIDEO_COUNT):
                youtubelist.insert(END, row, str(""))

        def Update():

            if len(You_tube_url.get()) != 0:
                youtube_api_backend.deleteRec(sd[0])
            if len(You_tube_url.get()) != 0:
                youtube_api_backend.addytdRec(YOU_ID, VIEW_COUNT, COMMENT_COUNT, SUBSCRIBER_COUNT, HIDDEN_SUBSCRIBER_COUNT, VIDEO_COUNT)
                youtubelist.delete(0, END)
                youtubelist.insert(END, (YOU_ID, VIEW_COUNT, COMMENT_COUNT, SUBSCRIBER_COUNT, HIDDEN_SUBSCRIBER_COUNT, VIDEO_COUNT))
  
        def search_customer():
            search_customers = Tk()
            search_customers.title("search record")

        def clickMe():
            self.label.configure(text = "you have selected " + myfruit.get())   

        # ====================================Frames=====================================
        MainFrame = Frame(self.root, bg="TEAL")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="GHOST WHITE", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('Times New Roman', 47, 'bold'), text="You Tube Information System",
                            bg="GHOST WHITE")
        self.lblTit.grid(sticky=W)

        ButtonFrame = Frame(MainFrame, bd=2, width=10, height=10, padx=18, pady=10, bg='TEAL', relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=10, height=10, padx=20, pady=20, relief=RIDGE, bg='GHOST WHITE')
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg='light blue',
                                   font=('comic sans MS', 20, 'bold'), text='student details:-\n')
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=670, height=680, padx=31, pady=3, relief=RIDGE,
                                    bg='Ghost white', font=('comic sans MS', 30, 'bold'), text='Fetched Data:-\n')
        DataFrameRIGHT.pack(side=RIGHT)

        # ===============================================LABELS AND ENTRY WIDGET=======================================================

        self.lblYou_tube_url = Label(DataFrameLEFT, font=('COMIC SANS MS', 20, 'bold'), text="Enter youtube link:",
                                     padx=2, pady=2, bg="ORANGE")
        self.lblYou_tube_url.grid(row=0, column=0, sticky=W)
        self.txtYou_tube_url = Entry(DataFrameLEFT, font=('COMIC SANS MS', 20, 'bold'), textvariable=You_tube_url,
                                     width=39)
        self.txtYou_tube_url.grid(row=0, column=1)

        youtube = apiclient.discovery.build('youtube', 'v3', developerKey=api_key)
        req = youtube.search().list(part='snippet', q='drop down in python programming', maxResults=50,
                                  type='channel').execute()
        my_list = []  # q=.get() vali
        for item in req['items']:
             my_list.append(item['snippet']['channelId'])

        self.drop = ttk.Combobox(DataFrameLEFT,width = 15, value=my_list) 
        self.drop.current(0)
        self.drop.grid(row=0,column=2)

        self.button = ttk.Button(DataFrameLEFT, width=15, text = "Select", command = clickMe)
        self.button.grid(row =1 , column =2)


        # ==================================================================listBox & scrollBar widget=====================================================
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        youtubelist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial', 12, 'bold'),
                              yscrollcommand=scrollbar.set)
        youtubelist.bind('<<ListboxSelect>>', youtubeRec)
        youtubelist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=youtubelist.yview)
        # ===============================================================Button Width======================================================

        self.btnAddData = Button(ButtonFrame, text="Add New", font=('times new roman', 20, 'bold'), height=3, width=13,
                                 bd=4, command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnAddData = Button(ButtonFrame, text="Display", font=('times new roman', 20, 'bold'), height=3, width=13,
                                 bd=4, command=DisplayData)
        self.btnAddData.grid(row=0, column=1)

        self.btnAddData = Button(ButtonFrame, text="Clear", font=('times new roman', 20, 'bold'), height=3, width=13,
                                 bd=4, command=clearData)
        self.btnAddData.grid(row=0, column=2)

        self.btnAddData = Button(ButtonFrame, text="Delete", font=('times new roman', 20, 'bold'), height=3, width=13,
                                 bd=4, command=DeleteData)
        self.btnAddData.grid(row=0, column=3)

        self.btnAddData = Button(ButtonFrame, text="Search", font=('times new roman', 20, 'bold'), height=3, width=13,
                                 bd=4, command=SearchDatabase)
        self.btnAddData.grid(row=0, column=4)

        self.btnAddData = Button(ButtonFrame, text="Update", font=('times new roman', 20, 'bold'), height=3, width=13,
                                 bd=4, command=Update)
        self.btnAddData.grid(row=0, column=5)

        self.btnAddData = Button(ButtonFrame, text="Exit", font=('times new roman', 20, 'bold'), height=3, width=13,
                                 bd=4, command=iExit)
        self.btnAddData.grid(row=0, column=6)






if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
