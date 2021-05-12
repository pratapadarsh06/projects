# Frontend

from tkinter import *
from tkinter import ttk
from typing import List, Any

import apiclient.discovery
import tkinter.messagebox
import urllib.request
import youtube_api_backend
from PIL import ImageTk, Image
from datetime import datetime
import json
import sys
import os
import tkinter as tk

api_key = "AIzaSyADsCqG71P_Xoesodbz-I-75wVh96QJk2w"

youtube = apiclient.discovery.build('youtube', 'v3', developerKey=api_key)


class hello:
    def __init__(self, root):

        def restart_program():
            os.system('python "D:\\sublime programs\\my1st.py"')
            sys.exit()

        def funky():
            self.root = root
            self.root.title("Search Screen (SCREEN 1)\n")

            self.img = Image.open('blue2.png')
            self.new_image = self.img.resize((1532, 835))
            self.new_image.save('blue2.png')

            self.new_image = ImageTk.PhotoImage(Image.open('blue2.png'))

            self.my_label = Label(image=self.new_image)
            self.my_label.place(relx=0, rely=0)

            You = StringVar()
            You_tube_url = StringVar()
            name = StringVar()
            start_Date = StringVar()
            end_Date = StringVar()
            TITLE = StringVar()
            SUBSCRIBER_COUNT = StringVar()
            VIEW_COUNT = StringVar()
            VIDEO_COUNT = StringVar()
            COMMENT_COUNT = StringVar()
            HIDDEN_SUBSCRIBER_COUNT = StringVar()
            YOU_ID = StringVar()
            PUBLISHED_AT = StringVar()

            self.l1 = ttk.Label(self.root, font=('Times New Roman', 9, 'bold'), text="search your choice :")
            self.l1.place(relx=0.2093, rely=0.512)

            self.l2 = ttk.Label(self.root, font=('Times New Roman', 9, 'bold'), text="End Date :")
            self.l2.place(relx=0.5, rely=0.7)

            self.l3 = ttk.Label(self.root, font=('Times New Roman', 9, 'bold'), text="Starting Date :")
            self.l3.place(relx=0.3, rely=0.7)

            self.txtYou_tube_url = Entry(font=('COMIC SANS MS', 20, 'bold'), textvariable=You_tube_url, width=39)
            self.txtYou_tube_url.place(relx=0.3, rely=0.5)

            self.txtstart_Date = Entry(font=('COMIC SANS MS', 20, 'bold'), textvariable=start_Date, width=10)
            self.txtstart_Date.place(relx=0.3, rely=0.75)

            self.txtend_Date = Entry(font=('COMIC SANS MS', 20, 'bold'), textvariable=end_Date, width=10)
            self.txtend_Date.place(relx=0.5, rely=0.75)

            def fun():
                if len(start_Date.get()) and len(end_Date.get()) != 0:
                    start_time_date = datetime.strptime(str(start_Date.get()), "%d/%m/%Y")
                    start_time = datetime(year=start_time_date.year, month=start_time_date.month,
                                          day=start_time_date.day).strftime('%Y-%m-%dT%H:%M:%SZ')
                    end_time_date = datetime.strptime(str(end_Date.get()), "%d/%m/%Y")
                    end_time = datetime(year=end_time_date.year, month=end_time_date.month,
                                        day=end_time_date.day).strftime('%Y-%m-%dT%H:%M:%SZ')
                    req = youtube.search().list(part='snippet', q=You_tube_url.get(), maxResults=50, type='video',
                                                publishedAfter=start_time, publishedBefore=end_time).execute()
                else:
                    req = youtube.search().list(part='snippet', q=You_tube_url.get(), maxResults=50,
                                                type='video').execute()
                my_list = []
                for item in req['items']:
                    my_list.append(item['snippet']['title'])

                self.combo = ttk.Combobox(font=('Times New Roman', 15), width=60, textvariable=You_tube_url,
                                          )
                self.combo['values'] = my_list
                self.combo.place(relx=0.3, rely=0.552)
                name = self.combo.get()

                # req = youtube.search().list(part='snippet', q=You_tube_url.get(), maxResults=50,
                #                            type='video').execute()

                def pilo():
                    # self.root = root
                    # self.root.title("SCREEN 2")
                    # self.root.geometry("1350x750+0+0")
                    # self.root.config(bg="cadet blue")

                    # ====================================Functions===============================================================

                    def iExit():
                        iExit = tkinter.messagebox.askyesno("You Tube Information System",
                                                            "confirm if you want to exit")
                        if iExit > 0:
                            root.destroy()
                            return

                    def clearData():
                        self.txtYou_tube_url.delete(0, END)

                    def addData():

                        if len(name) != 0:
                            for item in req['items']:
                                if name == item['snippet']['title']:
                                    You_tube_url = item['snippet']['channelId']
                                    break

                            data = urllib.request.urlopen(
                                "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + You_tube_url.get() + "&key=" + api_key).read()
                            SUBSCRIBER_COUNT = " SUBSCRIBER_COUNT : " + str(
                                json.loads(data)['items'][0]["statistics"]["subscriberCount"])
                            VIEW_COUNT = "  VIEW_COUNT : " + str(
                                json.loads(data)['items'][0]["statistics"]["viewCount"])
                            VIDEO_COUNT = "  VIDEO_COUNT : " + str(
                                json.loads(data)['items'][0]["statistics"]["videoCount"])
                            COMMENT_COUNT = "  COMMENT_COUNT : " + str(
                                json.loads(data)['items'][0]["statistics"]["commentCount"])
                            HIDDEN_SUBSCRIBER_COUNT = "  HIDDEN_SUBSCRIBER_COUNT : " + str(
                                json.loads(data)['items'][0]["statistics"]["hiddenSubscriberCount"])
                            YOU_ID = "  Channel ID : " + str(You_tube_url)
                            TITLE = " VIDEO TITLE :" + str(item['snippet']['title'])
                            PUBLISHED_AT = " PUBLISHED_AT :" + str(item['snippet']['publishedAt'])
                            youtube_api_backend.youtube_data()
                            youtube_api_backend.addytdRec(TITLE, PUBLISHED_AT, YOU_ID, VIEW_COUNT, COMMENT_COUNT,
                                                          SUBSCRIBER_COUNT, HIDDEN_SUBSCRIBER_COUNT, VIDEO_COUNT)
                            youtubelist.delete(0, END)
                            youtubelist.insert(END, (
                                TITLE, PUBLISHED_AT, YOU_ID, VIEW_COUNT, COMMENT_COUNT, SUBSCRIBER_COUNT,
                                HIDDEN_SUBSCRIBER_COUNT, VIDEO_COUNT))

                    def DisplayData():
                        youtubelist.delete(0, END)
                        for row in youtube_api_backend.viewData():
                            youtubelist.insert(END, row, str(""))

                    def youtubeRec(event):
                        global sd
                        searchYtd = youtubelist.curselection()[0]
                        sd = youtubelist.get(searchYtd)

                        self.txtYou_tube_url.delete(0, END)
                        self.txtYou_tube_url.insert(END, sd[0])

                    def DeleteData():
                        if len(You_tube_url.get()) != 0:
                            youtube_api_backend.deleteRec(sd[1])
                            clearData()
                            DisplayData()

                    def SearchDatabase():
                        youtubelist.delete(0, END)
                        for row in youtube_api_backend.searchData(sd[0]):
                            youtubelist.insert(END, row, str(""))

                    def Sorting():

                        def youtubeRec2(event):
                            global sd2
                            searchYtd2 = youtubelist2.curselection()[0]
                            sd2 = youtubelist2.get(searchYtd2)

                        scrollbar2 = Scrollbar(root)
                        scrollbar2.place(relx=0.002, rely=0.5)

                        youtubelist2 = Listbox(width=177, height=45, font=('arial', 12, 'bold'),
                                               yscrollcommand=scrollbar.set)
                        youtubelist2.bind('<<ListboxSelect>>', youtubeRec2)
                        youtubelist2.place(relx=0.02, rely=0.18)
                        scrollbar2.config(command=youtubelist2.yview)

                        youtubelist2.delete(0, END)
                        for row in youtube_api_backend.SortData():
                            youtubelist2.insert(END, row, str(""))

                    # ====================================Frames=====================================
                    MainFrame = Frame(self.root, bg="TEAL")
                    MainFrame.grid()

                    TitFrame = Frame(MainFrame, bd=2, padx=10, pady=8, bg="black", relief=RIDGE)
                    TitFrame.pack(side=TOP)

                    self.lblTit = Label(TitFrame, font=('Times New Roman', 47, 'bold'), text="Implementation page",
                                        bg="white")
                    self.lblTit.grid(sticky=W)

                    ButtonFrame = Frame(MainFrame, bd=2, width=10, height=10, padx=18, pady=10, bg='TEAL', relief=RIDGE)
                    ButtonFrame.pack(side=BOTTOM)

                    DataFrame = Frame(MainFrame, bd=1, width=10, height=10, padx=20, pady=20, relief=RIDGE, bg='grey')
                    DataFrame.pack(side=BOTTOM)

                    DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg='red',
                                               font=('comic sans MS', 20, 'bold'), text='student details:-\n')
                    DataFrameLEFT.pack(side=LEFT)

                    DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=670, height=680, padx=31, pady=3, relief=RIDGE,
                                                bg='dark blue', font=('comic sans MS', 30, 'bold'),
                                                text='Fetched Data:-\n')
                    DataFrameRIGHT.pack(side=RIGHT)

                    # ===============================================LABELS AND ENTRY WIDGET=======================================================

                    self.lblYou_tube_url = Label(DataFrameLEFT, font=('COMIC SANS MS', 20, 'bold'),
                                                 text="Enter youtube link:",
                                                 padx=2, pady=2, bg="red")
                    self.lblYou_tube_url.grid(row=0, column=0, sticky=W)
                    self.txtYou_tube_url = Entry(DataFrameLEFT, font=('COMIC SANS MS', 20, 'bold'),
                                                 textvariable=You_tube_url,
                                                 width=39)
                    self.txtYou_tube_url.grid(row=0, column=1)

                    self.screen2 = ttk.Button(DataFrameLEFT, width=20, text="go to search screen ",
                                              command=restart_program)
                    self.screen2.grid(row=4, column=1)

                    # ==================================================================listBox & scrollBar widget=====================================================
                    scrollbar = Scrollbar(DataFrameRIGHT)
                    scrollbar.grid(row=0, column=1, sticky='ns')

                    youtubelist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial', 12, 'bold'),
                                          yscrollcommand=scrollbar.set)
                    youtubelist.bind('<<ListboxSelect>>', youtubeRec)
                    youtubelist.grid(row=0, column=0, padx=8)
                    scrollbar.config(command=youtubelist.yview)
                    # ===============================================================Button Width======================================================

                    self.btnAddData = Button(ButtonFrame, text="Add New", font=('times new roman', 20, 'bold'),
                                             height=6, width=13,
                                             bd=4, command=addData)
                    self.btnAddData.grid(row=0, column=0)

                    self.btnAddData = Button(ButtonFrame, text="Display", font=('times new roman', 20, 'bold'),
                                             height=6, width=13,
                                             bd=4, command=DisplayData)
                    self.btnAddData.grid(row=0, column=1)

                    self.btnAddData = Button(ButtonFrame, text="Clear", font=('times new roman', 20, 'bold'), height=6,
                                             width=13,
                                             bd=4, command=clearData)
                    self.btnAddData.grid(row=0, column=2)

                    self.btnAddData = Button(ButtonFrame, text="Delete", font=('times new roman', 20, 'bold'), height=6,
                                             width=13,
                                             bd=4, command=DeleteData)
                    self.btnAddData.grid(row=0, column=3)

                    self.btnAddData = Button(ButtonFrame, text="Search", font=('times new roman', 20, 'bold'), height=6,
                                             width=13,
                                             bd=4, command=SearchDatabase)
                    self.btnAddData.grid(row=0, column=4)

                    self.btnAddData = Button(ButtonFrame, text="Sorting", font=('times new roman', 20, 'bold'),
                                             height=6, width=13,
                                             bd=4, command=Sorting)
                    self.btnAddData.grid(row=0, column=5)

                    self.btnAddData = Button(ButtonFrame, text="Exit", font=('times new roman', 20, 'bold'), height=6,
                                             width=13,
                                             bd=4, command=iExit)
                    self.btnAddData.grid(row=0, column=6)

                self.l2 = ttk.Label(self.root, font=('Times New Roman', 9, 'bold'),
                                    text="<----press select one more time")
                self.l2.place(relx=0.8, rely=0.515)

                self.screen2 = tk.Button(width=25, height=5, text="go to 2nd screen   ----->", command=pilo)
                self.screen2.place(relx=0.8, rely=0.8)

            self.screen1 = tk.Button(width=15, height=2, text="Select", command=fun)
            self.screen1.place(relx=0.71, rely=0.502)

        funky()


if __name__ == '__main__':
    # app = tk.Tk()
    root = tk.Tk()
    application = hello(root)
    root.mainloop()
