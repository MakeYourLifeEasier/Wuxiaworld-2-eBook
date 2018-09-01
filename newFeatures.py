from bs4 import BeautifulSoup
import sqlite3
import requests

completed   = "https://www.wuxiaworld.com/tag/completed"
chinese     = "https://www.wuxiaworld.com/language/chinese"
korean      = "https://www.wuxiaworld.com/language/korean"
original    = "https://www.wuxiaworld.com/language/english"


def updateDB(link, table_name):
    # ToDo: Maybe db open outsite of function
    # ToDo: check if database is available
    conn = sqlite3.connect("test.db") # Placeholder used
    cursor = conn.cursor()
    sql_create = '''
    CREATE TABLE {} (name TEXT, link TEXT, synopsis TEXT, img BLOB)'''.format(table_name)
    cursor.execute(sql_create)
    conn.commit()
    response = requests.get(link)

    soup = BeautifulSoup(response.content, "lxml")
    media = soup.find_all("li", class_="media")
    # Go through each entry and get content
    for i in range(len(media)):
        img_link = media[i].find("img").get("src")
        novel_link = "https://www.wuxiaworld.com" + media[i].find("a", class_="text-white").get("href")
        novel_name = media[i].find("a", class_="text-white").replace("\n", "")
        novel_synopsis = media[i].find("p").text
        img = sqlite3.Binary(requests.get(img_link).content)
        sql_insert = '''
        INSERT INTO info (name, link, synopsis, img) VALUES (?, ?, ?, ?)'''
        cursor.execute(sql_insert, (novel_name, novel_link, novel_synopsis, img))

    conn.commit()
    conn.close()


updateDB(completed, "completed")