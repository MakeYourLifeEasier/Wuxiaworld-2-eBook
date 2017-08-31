import links
import getify
import sqlite3 as sql
import tkinter as tk
from tkinter import ttk

#Initializing Stuff
main = tk.Tk()
main.title("Wuxiaworld-2-eBook")
main.geometry("375x150")
main.resizable(False, False)
app = tk.Frame(main)
app.grid()
conn = sql.connect("novels.db")
c = conn.cursor()

#Enables book number field only on novels that are using it
def on_field_change(index, value, op):
    if novel.get() in hasbook:
        book_number_chosen.configure(state = "enabled")
    else:
        book_number_chosen.configure(state = "disabled")

def button_press():
    #Getting Information
    generate_button.configure(state = "disabled")
    s_chapter = starting_chapter.get()
    reset = str(s_chapter)
    e_chapter = ending_chapter.get()
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

    #Calls function's for downloading, cleanup and managing
    #a list of file name's for cleanup, ToC and packing
    y = int(s_chapter)
    file_list = []
    for x in range(len(bulk_list)):
        getify.download(bulk_list[x], str(s_chapter) + ".xhtml")
        getify.clean(str(s_chapter) + ".xhtml", raw_info[2] + str(s_chapter), '<div itemprop="articleBody"', '''<div class="code-block''')
        file_list.append(raw_info[2] + str(s_chapter) + ".xhtml")
        s_chapter = int(s_chapter) + 1

    getify.generate(file_list, raw_info[0], raw_info[3], raw_info[2], reset, str(e_chapter))
    generate_button.configure(state = "enabled")


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

#Code for "Generate" button
generate_button = ttk.Button(app, text = "Generate", command = button_press)
generate_button.grid(column = 1, row = 4, sticky = "E")

main.mainloop()
