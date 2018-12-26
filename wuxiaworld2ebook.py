import getify
import sqlite3 as sql
import tkinter as tk
from tkinter import ttk
from urllib.error import HTTPError, URLError
import os
import json
from os import path

#Initializing Stuff

main = tk.Tk()
main.title("Wuxiaworld-2-eBook")
main.geometry("535x190")
main.resizable(True, True)
app = tk.Frame(main)
app.grid()
conn = sql.connect("novels.db")
c = conn.cursor()

#Enables book number field only on novels that are using it
def on_field_change(index, value, op):
    try:
        if novel.get() in hasbook:
            book_number_chosen.configure(state = "enabled")
        else:
            book_number_chosen.configure(state = "disabled")
    except:
        pass

def button_press():
    try:
        #Getting Information
        generate_button.configure(state = "disabled")
        s_chapter = starting_chapter.get()
        reset = str(s_chapter)
        e_chapter = ending_chapter.get()
        cleanup = delete_chapters.get()
        booknr = book_number.get()
        name = novel.get()

        #Getting relevant novel Information
        raw_info = []
        for i in db:
            if name in i[0]:
                raw_info.append(i)
        raw_info = raw_info[0]
        if raw_info[5] == 0:
            link = raw_info[1]
        else:
            link = raw_info[1] + str(booknr) + "-chapter-"

        #Generating list with download links
        bulk_list = []
        for s_chapter in range(s_chapter, e_chapter + 1):
            bulk_list.append(link + str(s_chapter))
        s_chapter = reset

        getify.cover_generator(raw_info[4], s_chapter, str(e_chapter))

        if not path.exists(raw_info[0]):
            os.makedirs(raw_info[0])

        #Calls function's for downloading, cleanup and managing
        #a list of file name's for cleanup, ToC and packing
        y = int(s_chapter)
        file_list = []
        for x in range(len(bulk_list)):
            if path.exists(_get_xhtml_path(raw_info, s_chapter)):
                print(_get_xhtml_path(raw_info, s_chapter), " already exists")
            else:
                try:
                    getify.download(bulk_list[x], str(s_chapter) + ".xhtml")
                    file_list.append(_get_xhtml_path(raw_info, s_chapter))
                except HTTPError as e:
                    # Return code error (e.g. 404, 501, ...)
                    print('URL: {}, HTTPError: {} - {}'.format(bulk_list[x], e.code, e.reason))
                except URLError as e:
                    # Not an HTTP-specific error (e.g. connection refused)
                    print('URL: {}, URLError: {}'.format(bulk_list[x], e.reason))
                else:
                    getify.clean(str(s_chapter) + ".xhtml", _get_xhtml_path(raw_info, s_chapter), name)
            s_chapter = int(s_chapter) + 1

        getify.generate(file_list, raw_info[0], raw_info[3], raw_info[2], reset, str(e_chapter), cleanup=cleanup)

    finally:
        generate_button.configure(state = "enabled")

def _get_xhtml_path(raw_info, s_chapter, extension=".xhtml"):
    return path.join(raw_info[0], raw_info[2] + str(s_chapter) + extension)

#Getting information from Database
c.execute("SELECT * FROM 'Information'")
db = c.fetchall()
namelist = []
hasbook = []
for i in db:
    namelist.append(i[0])
    if i[5] == 1:
        hasbook.append(i[0])
namelist.sort()

#Load config
config_file = open("config.json", "r")
app_config = json.loads(config_file.read())
config_file.close()

#Code for the Combobox and the label
label1 = ttk.Label(app, text = "Select Novel:")
label1.grid(column = 0, row = 0, pady = 10, sticky = "W")
novel = tk.StringVar()
novel_chosen = ttk.Combobox(app, width = 42, textvariable = novel, state = "readonly")
novel.trace("w", on_field_change)
novel_chosen["values"] = namelist
novel_chosen.grid(column = 1, row = 0)
novel_chosen.current(0)

#Code for the Book Entry and label
label2 = ttk.Label(app, text = "Book Number: ")
label2.grid(column = 0, row = 1, sticky = "W")
book_number = tk.IntVar()
book_number_chosen = ttk.Entry(app, width = 5, textvariable = book_number, state = "disabled")
book_number_chosen.grid(column = 1, row = 1, sticky = "W")

#Code for the starting chapter Entry and label
label3 = ttk.Label(app, text = "Starting Chapter: ")
label3.grid(column = 0, row = 2, pady = 10, sticky = "W")
starting_chapter = tk.IntVar()
starting_chapter_chosen = ttk.Entry(app, width = 5, textvariable = starting_chapter)
starting_chapter_chosen.grid(column = 1, row = 2, sticky = "W")

#Cpde fpr the ending chapter Entry and label
label4 = ttk.Label(app, text = "Ending Chapter: ")
label4.grid(column = 0, row = 3, sticky = "W")
ending_chapter = tk.IntVar()
ending_chapter_chosen = ttk.Entry(app, width = 5, textvariable = ending_chapter)
ending_chapter_chosen.grid(column = 1, row = 3, sticky = "W")

#Code for delete chapters
label5 = ttk.Label(app, text = "Delete temporary chapter files after download: ")
label5.grid(column = 0, row = 4, pady = 10, sticky = "W")
delete_chapters = tk.BooleanVar()
delete_chapters.set(app_config["default_temporary_chapter_cleanup_behavior"])
delete_chapters_chosen = ttk.Checkbutton(app, variable = delete_chapters, offvalue=False, onvalue=True)
delete_chapters_chosen.grid(column =1, row = 4, sticky = "W")

#Code for "Generate" button
generate_button = ttk.Button(app, text = "Generate", command = button_press)
generate_button.grid(column = 1, row = 5, sticky = "E")



if __name__=="__main__":
    main.mainloop()
