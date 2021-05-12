# backend
import sqlite3


def youtube_data():
    con = sqlite3.connect("youtube6.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS new1_youtube (TITLE TEXT , YOU_ID TEXT PRIMARY KEY,PUBLISHED_AT VARCHAR, VIEW_COUNT INTEGER,COMMENT_COUNT INTEGER, SUBSCRIBER_COUNT INTEGER,HIDDEN_SUBSCRIBER_COUNT INTEGER,VIDEO_COUNT INTEGER)")
    con.commit()
    con.close()


def addytdRec(TITLE, PUBLISHED_AT, YOU_ID, VIEW_COUNT, COMMENT_COUNT, SUBSCRIBER_COUNT, HIDDEN_SUBSCRIBER_COUNT,
              VIDEO_COUNT):
    con = sqlite3.connect("youtube6.db")
    cur = con.cursor()
    cur.execute("INSERT INTO new1_youtube VALUES (?,?,?,?,?,?,?,?)",
                (TITLE, PUBLISHED_AT, YOU_ID, VIEW_COUNT, COMMENT_COUNT, SUBSCRIBER_COUNT,
                 HIDDEN_SUBSCRIBER_COUNT, VIDEO_COUNT))
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect("youtube6.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM new1_youtube")
    rows = cur.fetchall()
    con.close()
    return rows


def deleteRec(YOU_ID):
    con = sqlite3.connect("youtube6.db")
    cur = con.cursor()
    cur.execute("DELETE FROM new1_youtube WHERE YOU_ID=?", (YOU_ID,))
    con.commit()
    con.close()


def searchData():
    con = sqlite3.connect("youtube6.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM new1_youtube WHERE TITLE=?", (TITLE,))
    rows = cur.fetchall()
    con.close()
    return rows


def SortData():
    con = sqlite3.connect("youtube6.db")
    cur = con.cursor()
    cur.execute("SELECT *FROM new1_youtube ORDER BY TITLE")
    # cur.execute("SELECT * FROM new_youtube ORDER BY CONVERT(DateTime, PUBLISHED_AT,101)  DESC")
    rows = cur.fetchall()
    con.close()
    return rows
