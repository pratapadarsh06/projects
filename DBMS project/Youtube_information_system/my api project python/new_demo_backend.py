# backend
import sqlite3


def youtube_data():
    con = sqlite3.connect("youtube.db")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS youtube (id VARCHAR(20) PRIMARY KEY,VIEW_COUNT INTEGER,COMMENT_COUNT INTEGER,"
        "SUBSCRIBER_COUNT INTEGER,HIDDEN_SUBSCRIBER_COUNT INTEGER,VIDEO_COUNT INTEGER)")
    con.commit()
    con.close()


def addytdRec(VIEW_COUNT, COMMENT_COUNT, SUBSCRIBER_COUNT, HIDDEN_SUBSCRIBER_COUNT, VIDEO_COUNT):
    con = sqlite3.connect("youtube.db")
    cur = con.cursor()
    cur.execute("INSERT INTO youtube VALUES (NULL,?,?,?,?,?)", (VIEW_COUNT, COMMENT_COUNT, SUBSCRIBER_COUNT,
                                                                HIDDEN_SUBSCRIBER_COUNT, VIDEO_COUNT))
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect("youtube.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM youtube")
    rows = cur.fetchall()
    con.close()
    return rows


def deleteRec(id):
    con = sqlite3.connect("youtube.db")
    cur = con.cursor()
    cur.execute("DELETE FROM youtube WHERE id=?", (id,))
    con.commit()
    con.close()


def searchData(VIEW_COUNT="", COMMENT_COUNT="", SUBSCRIBER_COUNT="", HIDDEN_SUBSCRIBER_COUNT="", VIDEO_COUNT=""):
    con = sqlite3.connect("youtube.db")
    cur = con.cursor()
    cur.execute("SELECT *FROM YOUTUBE WHERE ID=? OR VIEW_COUNT=? OR COMMENT_COUNT=? OR SUBSCRIBER_COUNT=? OR "
                "HIDDEN_SUBSCRIBER_COUNT=? OR VIDEO_COUNT=?",
                (ID, VIEW_COUNT, COMMENT_COUNT, SUBSCRIBER_COUNT, HIDDEN_SUBSCRIBER_COUNT, VIDEO_COUNT))
    rows = cur.fetchall()
    con.close()
    return rows


def dataUpdate(id, VIEW_COUNT="", COMMENT_COUNT="", SUBSCRIBER_COUNT="", HIDDEN_SUBSCRIBER_COUNT="", VIDEO_COUNT=""):
    con = sqlite3.connect("youtube.db")
    cur = con.cursor()
    cur.execute("UPDATE YOUTUBE SET VIEW_COUNT=?, COMMENT_COUNT=?, SUBSCRIBER_COUNT=?, "
                "HIDDEN_SUBSCRIBER_COUNT=?, VIDEO_COUNT=?,WHERE id=?",
                (VIEW_COUNT, COMMENT_COUNT, SUBSCRIBER_COUNT, HIDDEN_SUBSCRIBER_COUNT, VIDEO_COUNT, id))
    con.commit()
    con.close()
