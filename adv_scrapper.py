"""
This is a python program for web scrapping made by <Mohd Farhaad> from Innobuz
"""

"""
to improve things:
    1.)proper links with acceble in one click
    2.)social media links should be seprate
    3.)code to start the mysql server
    4.)entering the full articles 
    5.)giving meaningful variable
    6.)commenting the useless print statements
    7.)not all links are adding in the databse

"""

#required modules
import requests
from bs4 import BeautifulSoup
import mysql.connector
import subprocess

# #starting the mysql server
# b = subprocess.call(["mysql", "-u", "root","-p", "passpass"])

#CONNECTING TO THE DATABSE
mydb = mysql.connector.connect(host="localhost", user="bill" , password = "passpass", database = 'test',port="3306")
cur = mydb.cursor()
delete_table = cur.execute("DROP TABLE scrapped_data")
print("no")
create_table = cur.execute("CREATE TABLE scrapped_data(website_url VARCHAR(100), title varchar(100), article varchar(1000), links varchar(1000))")
print("yes")

url = "https://www.codewithharry.com"

def htmlfile(url, path): #function to get the webpage, save it in a file
    try:
        r = requests.get(url)
        with open(path, 'w') as f:
            b = f.write(r.text)
    except Exception as e:
        print("this code is a disappointment")

try:
    htmlfile(url, "file.html")
except Exception as e:
    print("sorry for the issue!!")

with open("file.html", "r") as f:
    file = f.read()
soup = BeautifulSoup(file,"html.parser")

#getting the title
title = soup.find('title').get_text()
print(title)

#getting the links available ion the page
anchors = soup.find_all("a")
for item in anchors:
    links = item.get("href")
    print(url+links)

#getting the paragrah    
para = soup.find("p").get_text()
print(para)

#entering the data 
sql = "INSERT INTO scrapped_data (website_url, title, article, links)VALUES (%s,%s,%s,%s)"
val = (url, title, para, links)
n = cur.execute(sql, val)
mydb.commit()

print(n)
print("yes")

#taking out data from the database
try:
    h = input("do you wanna scrap:- ")
    while "yes" in h:
        query = input("enter what you want:- ")
        if "title" in query:
            k ="SELECT title FROM scrapped_data"
            cur.execute(k)
            myresult = cur.fetchall()
            print(myresult)
        elif "website_url" in query:
            k ="SELECT website_url FROM scrapped_data"
            cur.execute(k)
            myresult2 = cur.fetchall()
            print(myresult2)
        elif "article" in query:
            k ="SELECT article FROM scrapped_data"
            cur.execute(k)
            myresult3 = cur.fetchall()
            print(myresult3)
        elif "links" in query:
            k ="SELECT links FROM scrapped_data"
            cur.execute(k)
            myresult4 = cur.fetchall()
            print(myresult4)
        elif "exit" or "quit" in query:
            print("happy to help;)")
            break
        else:
            print("it is what it is!!")
except Exception as e:
    print(e)
