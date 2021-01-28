#!/usr/bin/env python3

import os
import json


#PRINT VARIABLES A PLAIN TEXT
print("Content-Type: text/plain") #specification that after this line, expect plain text
print()
print(os.environ) #if you just print this without the previous two lines the browser will give you a pop up trying to tell you to dl a script
#THEN TYPE IN A BROWSER localhost:8080/hello.py

#Make your CGI script serve the environment back as JSON
#PRINT VARIABLES AS JSON
print("Content-Type: application/json")
print()
print(json.dumps(dict(os.environ),indent = 2))

#TO ADD QUERY PARAMATERS
    #TYPE IN A BROWSER localhost:8080/hello.py?
    #after the question mark add a like query = yes OR hereisaquery
    #scroll down to the variable query string
    #whatever you put after the question mark

#Modify your CGI script to report the values of the query parameters in the HTML.
#Modify your CGI script to report the user’s browser in the HTML.
#PRINT QUERY PARAMETER DATA IN HTML - if we just want to look at the query string variable
print("Content-Type: text/html")
print()
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

#P = paragraph format
#os.environ is a query string

#QUESTION 4 - find the variable that prints the browser, replace QUERY_STRING with the variable name
#ANSWER IS USER AGENT - this is how to print browser info
print("Content-Type: text/html")
print()
print(f"<p>BROWSER_INFO={os.environ['HTTP_USER_AGENT']}</p>")



