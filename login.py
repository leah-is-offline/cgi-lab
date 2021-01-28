#!/usr/bin/env python3
import json

import cgi
import cgitb
cgitb.enable()

import templates
import secret
import os
from http.cookies import SimpleCookie

s = cgi.FieldStorage() #field storage object
username = s.getfirst("username") #saving possible information in html field
password = s.getfirst("password") #saving possible values in html field

form_ok = username == secret.username and password == secret.password


c = SimpleCookie(os.environ['HTTP_COOKIE'])
c_username = None
c_password = None

if c.get("username"):
    c_username = c.get("username").value
if c.get("password"):
    c_password = c.get("password").value

#Modify your CGI script to set a cookie if the login is correct.
cookie_ok = c_username == secret.username and c_password == secret.password
if cookie_ok:
    username = c_username
    password = c_password


print("Content-Type: text/html")
if form_ok:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")
print()


if not username and not password:
    print(templates.login_page())
elif username == secret.username and password == secret.password:
    #print the secret page is username and password provided are equal to secret credentials
    #Modify your CGI script so it displays a secret message if the cookie says the user is logged in. 
    print(templates.secret_page(username,password))
else:
    #Modify your CGI script to contain a login form that POSTs to itself. You may use login_page() in templates.py.
    #Modify your CGI script to report the values of the POSTed data in the HTML
        #print("username ", username)
        #print("password ", password)
    print(templates.after_login_incorrect())
    




