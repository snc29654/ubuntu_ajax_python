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

dbname = 'edict.sqlite3'
def diary_world(match_word):
    with closing(sqlite3.connect(dbname)) as conn:
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


print("Content-Type: text/html; charset=utf-8\n")


print(diary_world(str(zip_code)))
#print(find_data)

