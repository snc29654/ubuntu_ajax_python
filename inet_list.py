#!/usr/bin/python3
# -*- coding: utf-8 -*-

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

import re
import sys
import bs4
import requests
from urllib.parse import urljoin





cgitb.enable()
form=cgi.FieldStorage()
dbname='./'+ form.getvalue("sent4")

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

zip_code=[]
def  get_link(url):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "lxml")
    links = soup.select("a")

    keys = set()
    results = []
    for link in links:
        link_url = link.get("href")
        if not link_url:
            continue

        if not link_url.startswith("http"):
            link_url = urljoin(url, link_url)

        link_text = link.text
        if not link_text:
            link_text = ""
        link_text = link_text.strip()
        link_text = re.sub(r"\n", " ", link_text)

        key = link_url + link_text
        if key in keys:
            continue
        keys.add(key)

        results.append({"url": link_url, "text": link_text})

    return results


def  copy_link(url):
    results = get_link(url)

    text = ""
    for result in results:
        text +=  "<a href= \"" + result["url"] +  "\"" +" target=\"_blank\"" + "</a>"+result["text"] +"\t" +"<br>" +"\n"   
    return(text)


def  data_print(url):
    global zip_code

    params = {'p':zip_code,
          'search.x':'1',
          'fr':'top_ga1_sa',
          'tid':'top_ga1_sa',
          'ei':'UTF-8',
          'aq':'',
          'oq':'',
          'afs':'',}

    r = requests.get(url)

    data = BeautifulSoup(r.content, 'html.parser')
    find_data=data.find_all("a")
    return(find_data)



zip_code=form.getvalue("sent2")

find_data=copy_link(zip_code)

date = datetime.date.today()

name="URLリスト"
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
        
    scraping_contents=find_data
    Contents = str(scraping_contents)
    Contents = Contents.replace("\n","")
    Contents = Contents.replace("\t","")
    insert_sql = 'insert into users (date, name, weather, kind, zip_code,Contents) values (?,?,?,?,?,?)'
    users = [
    (date, name, weather, kind, zip_code,Contents)
    ]
    c.executemany(insert_sql, users)
    conn.commit()

print("Content-type: text/html\n")

print(find_data)
