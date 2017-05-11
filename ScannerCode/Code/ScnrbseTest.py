import requests
from bs4 import BeautifulSoup
import json
import os
import Email

shoplist = ['SHOPPING LIST']
while True:
    name = raw_input("Item?")
    if name == "Exit":
        break
    elif name == "Done":
        for car in shoplist:
            print car
            outfile = open('list.txt', 'a')
            outfile.write(car+'\n')
    elif name == "Clear":
        F = open('list.txt', 'w')
        F.write("")
        F.close()
    elif name == "ShoppingList":
        F = open('list.txt', 'r')
        print F.read()
    elif name == "ChangeEmail":
        F = open('emailtosend.txt', 'w')
        WF = raw_input('New Email?')
        F.write(WF)
    elif name == "email":
       F = open('emailtosend.txt', 'r')
       Email.sendmail(F.read())
       clear = raw_input("ClearList y/n?")
       if clear == 'y':
            F = open('list.txt', 'w')
            F.write("")
            F.close()
            print 'cleared'
    else:
        aResp = requests.get("http://www.upcitemdb.com/upc/" + name)
        soup = BeautifulSoup(aResp.text, "html5lib")

        item = soup.findAll('title')
        newitem = item[0]
        jtex = newitem.text
        actual = jtex[19:]
        print actual.replace('| upcitemdb.com', '')
                
        shoplist.append(actual.replace('| upcitemdb.com', ''))
        
