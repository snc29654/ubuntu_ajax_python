#!/home/username/my_project/cgi-bin/.venv/bin/python3
# -*- coding: utf-8 -*-

import cgi
import json

print("Content-Type: application/json; charset=utf-8")
print()  # 空行がヘッダとボディの区切り

form = cgi.FieldStorage()
name = form.getfirst("name", "world")

data = {"message": f"usernameシバン, {name}!"}
print(json.dumps(data, ensure_ascii=False))
