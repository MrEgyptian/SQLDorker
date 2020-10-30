#!/bin/python
'''
29-10-2020
Hello everybody i am ahmed 
and this is a simple opensource script 
for using google dorks for Testing SQL injection 
I hope you enjoy the code and have fun :)
'''
#Defining colors variables
r="\x1b[91m"
g="\x1b[92m"
ye="\x1b[93m"
w="\x1b[97m"
import requests						#For making the http requests
import readline						#For using keyboard keys correctly unside inputs 
import os,subprocess,re,time		#Other modules for using Operating system and regular expressions
from datetime import datetime		#For making time stamps
from urllib.parse import unquote	#For Decoding The URL
t="\r"

def cool(text):
	global t
	char=0
	while char<len(text):
		t=t+text[char]
		print(t,end="")
		time.sleep(0.1)
		char=char+1
		pass
print("""
\x1b[97m┌───────────────────────────────────────────────────────────────\x1b[97m┐
\x1b[97m│                                                               \x1b[97m│
\x1b[97m│\x1b[91m  ▄▄▄▄ \x1b[93m  ▄▄▄▄  \x1b[95m▄      \x1b[92m▄▄▄▄                 █                   \x1b[97m│
\x1b[97m│\x1b[91m █▀   ▀\x1b[93m ▄▀  ▀▄ \x1b[95m█      \x1b[92m█   ▀▄  ▄▄▄    ▄ ▄▄  █   ▄   ▄▄▄    ▄ ▄▄ \x1b[97m│
\x1b[97m│\x1b[91m ▀█▄▄▄ \x1b[93m █    █ \x1b[95m█      \x1b[92m█    █ █▀ ▀█   █▀  ▀ █ ▄▀   █▀  █   █▀  ▀\x1b[97m│
\x1b[97m│\x1b[91m     ▀█\x1b[93m █    █ \x1b[95m█      \x1b[92m█    █ █   █   █     █▀█    █▀▀▀▀   █    \x1b[97m│
\x1b[97m│\x1b[91m ▀▄▄▄█▀\x1b[93m  █▄▄█▀ \x1b[95m█▄▄▄▄▄ \x1b[92m█▄▄▄▀  ▀█▄█▀   █     █  ▀▄  ▀█▄▄▀   █    \x1b[97m│
\x1b[97m│\x1b[91m       \x1b[93m     █                                                  \x1b[97m│
\x1b[97m│\x1b[91m         Github:github.com/ahmedMahmed8a                       \x1b[97m│
\x1b[97m└───────────────────────────────────────────────────────────────┘

	""")
dork=str(input("\n\033[36;1m [%] Enter Google Dork: "))#getting the dork from user input
pag=0												   #Declaring number pages variable  
def pages():										   
	global pag
	try:
		pag=int(input("\033[36;1m[**] Enter Google Number of pages to scan: "))#
		pass
	except ValueError:
		print("Please write a right value")
		pages()
pages()
link="https://www.google.com/search?q="+dork+"&ie=utf-8&oe=utf-8&aq=t&start="+str(pag)+"0"#link to search in google
resp=requests.get(link).text #response text
x = resp.split("<a href=\"/url?q=")
links=""
for i in range(1,len(x)):
	links=links+unquote(x[i].split("&amp;")[0])+"%27\n"
	pass
checks=links.split("\n")
f=open("logs.txt","a+")#Opening logs.txt file to get results
f.write("\n\n\nScanning "+dork+"Number of pages "+str(pag)+" at ["+str(datetime.now())+"]\n This is the result of google:")
for i in range(1,len(checks)-1):
	check=requests.get(checks[i]).text
	if ("SQL syntax" in check or "MySQL" in check or "mysql_" in check or "argument is not" in check ):
		#checking the link
		print(g+"["+ye+"vuln"+g+"] "+r+checks[i])
		f.write(res[y])
	else:
		#If the link isn't vuln
		print(r+"["+g+"not vuln"+r+"] "+ye+checks[i])
	
	pass
cool(g+"The vuln websites are saved in "+ye+"logs.txt")
#	y=y+1