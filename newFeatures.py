from bs4 import BeautifulSoup
import sqlite3
import requests
import os

completed   = "https://www.wuxiaworld.com/tag/completed"
chinese     = "https://www.wuxiaworld.com/language/chinese"
korean      = "https://www.wuxiaworld.com/language/korean"
original    = "https://www.wuxiaworld.com/language/english"

os.remove("test2.db")

def updateDB(link, table_name):
    # ToDo: Maybe db open outsite of function
    # ToDo: check if database is available
    conn = sqlite3.connect("test2.db") # Placeholder used
    cursor = conn.cursor()
    sql_create = '''
    CREATE TABLE {} (name TEXT, link TEXT, synopsis TEXT, img BLOB)'''.format(table_name)
    cursor.execute(sql_create)
    conn.commit()
    response = requests.get(link)

    soup = BeautifulSoup(response.content, "lxml")
    p15 = soup.find("div", class_="p-15")
    media = p15.find_all("li", class_="media")
    # Go through each entry and get content
    for i in range(len(media)):
        img_link = media[i].find("img").get("src")
        if img_link[0] == "/":
            img_link = "https://www.wuxiaworld.com" + img_link
        elif img_link[0] is not "/" or img_link[0] is not "h" or img_link[0] is not "w":
            img_link = "https://i.imgur.com/uOGV7Us.jpg"
        novel_link = "https://www.wuxiaworld.com" + media[i].find("a", class_="text-white").get("href")
        novel_name = media[i].find("a", class_="text-white").text
        novel_synopsis_list = media[i].find_all("p")
        novel_synopsis = ""
        for x in range(len(novel_synopsis_list)):
            novel_synopsis = novel_synopsis + novel_synopsis_list[x].text
        img = sqlite3.Binary(requests.get(img_link).content)
        sql_insert = '''
        INSERT INTO {} (name, link, synopsis, img) VALUES (?, ?, ?, ?)'''.format(table_name)
        cursor.execute(sql_insert, (novel_name, novel_link, novel_synopsis, img))

    conn.commit()
    conn.close()


updateDB(completed, "completed")
updateDB(chinese, "chinese")
updateDB(korean, "korean")
updateDB(original, "original")