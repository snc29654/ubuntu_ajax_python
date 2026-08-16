#!/home/username/my_project/cgi-bin/.venv/bin/python3
# -*- coding: utf-8 -*-
import os
import cgi
import cgitb
import json
import sys
import io
import requests
from bs4 import BeautifulSoup
import sqlite3
from contextlib import closing
import datetime

cgitb.enable()
form=cgi.FieldStorage()
dbname='./'+ form.getvalue("sent4")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

zip_code=[]
zip_code=form.getvalue("sent2")

dbname_dict = 'edict.sqlite3'
def diary_world(match_word):
    with closing(sqlite3.connect(dbname_dict)) as conn:
        c = conn.cursor()
        create_table = '''create table items (item_id INTEGER PRIMARY KEY,word TEXT,mean TEXT,level INTEGER DEFAULT 0
)'''
        try:
            c.execute(create_table)
        except:
            #print("database already exist")
            pass
        #全レコード表示
        select_sql = 'select * from items where word = '+'"'+str(match_word)+'"'
        data=[]
        #print (select_sql )
        try:
            for row in c.execute(select_sql):
                #print(row)
                data.append(row)
                #ブラウザに改行を送付
                data.append("<br>")
            conn.commit()
        except:
            print("data not found")
    return str(data)

yaku =diary_world(str(zip_code)) 

date = datetime.date.today()

name="英和"
weather=""
kind=""

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()
    create_table = '''create table users (id INTEGER PRIMARY KEY,date varchar(64), name varchar(64),
                      weather varchar(64), kind varchar(32), zip_code varchar(64),Contents varchar(256))'''
    try:
        c.execute(create_table)
    except:
        pass
        
    scraping_contents=yaku
    Contents = str(scraping_contents)
    Contents = Contents.replace ("\n","")
    Contents = Contents.replace ("\t","")
    memo_title="<font color=\"red\">"  + zip_code + "</font>" + "<br>"
    memo_title=memo_title.replace("\u3000"," ")
    insert_sql = 'insert into users (date, name, weather, kind, zip_code,Contents) values (?,?,?,?,?,?)'
    users = [
    (date, name, memo_title, kind, weather,Contents)
    ]
    c.executemany(insert_sql, users)
    conn.commit()




print("Content-Type: text/html; charset=utf-8\n")

print(yaku)
#print(find_data)

