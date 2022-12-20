import json
import requests
import datetime
import csv
import time
from datetime import datetime
import pandas as pd
#THIS TOOL MADED BY 0xSp3aR
#CONTACT 0xSp3ar#5560
keyword =""
tag=""
api=str(input('''
    ___________________  __
   / ____/_  __/ ___/\ \/ /
  / __/   / /  \__ \  \  / 
 / /___  / /  ___/ /  / /  
/_____/ /_/  /____/  /_/                              
                        By 0xSp3ar#5560
Get You Api From https://www.etsy.com/developers/register
NOTE : SHOULD BE ACTIVE

Enter Your Api : '''))

method_search=str(input('''
1 - Search By keyword
2 - Search By Tag 
3 - Search By Keyword + Tag
Enter Number :'''))

all_or_no = str(input('''
1 - all
2 - only digital
'''))
cool = ['vw','fav','Date','Qnt','price','title','url']
with open(f'Done.csv' , 'a', encoding='utf8') as done:
        writer = csv.writer(done)
        writer.writerow(cool)
ok = slice(0,-13)
sort_on = ['created', 'price', 'score']

def keyword_digital(keyword,api):
    for page in range(1,501):
        r = requests.get(f'https://openapi.etsy.com/v2/listings/active?keywords={keyword}&limit=100&page={page}&is_digital=1&api_key={api}').text 
        time.sleep(0.5)
        data = json.loads(r)
        for i in data['results']:

                title = i['title']
                creation = i.get('original_creation_tsz')
                date = str(pd.to_datetime(datetime.today()).date() - pd.to_datetime(datetime.fromtimestamp(creation)).date())
                days=date[ok]
                price = i.get('price')
                quantity = i.get('quantity')
                views = i.get('views')
                num_favorers = i.get('num_favorers')
                url = i.get('url')
                                
                cool = [views,num_favorers,days,quantity,price,title,url]
                with open(f'Done.csv' , 'a', encoding='utf8') as done:
                        writer = csv.writer(done)
                        writer.writerow(cool)
        r=""        
def keywordall(keyword,api):
    for page in range(1,501):
        r = requests.get(f'https://openapi.etsy.com/v2/listings/active?keywords={keyword}&limit=100&page={page}&api_key={api}').text
        time.sleep(0.5)
        data = json.loads(r)
        for i in data['results']:

                title = i['title']
                creation = i.get('original_creation_tsz')
                date = str(pd.to_datetime(datetime.today()).date() - pd.to_datetime(datetime.fromtimestamp(creation)).date())
                days=date[ok]
                price = i.get('price')
                quantity = i.get('quantity')
                views = i.get('views')
                num_favorers = i.get('num_favorers')
                url = i.get('url')
                                
                cool = [views,num_favorers,days,quantity,price,title,url]
                with open(f'Done.csv' , 'a', encoding='utf8') as done:
                        writer = csv.writer(done)
                        writer.writerow(cool)
        r=""        
def tagdigital(tag,api):
    for page in range(1,501):
        r = requests.get(f'https://openapi.etsy.com/v2/listings/active?tags={tag}&limit=100&page={page}&is_digital=1&api_key={api}').text
        time.sleep(0.5)
        data = json.loads(r)
        for i in data['results']:

                title = i['title']
                creation = i.get('original_creation_tsz')
                date = str(pd.to_datetime(datetime.today()).date() - pd.to_datetime(datetime.fromtimestamp(creation)).date())
                days=date[ok]
                price = i.get('price')
                quantity = i.get('quantity')
                views = i.get('views')
                num_favorers = i.get('num_favorers')
                url = i.get('url')
                                
                cool = [views,num_favorers,days,quantity,price,title,url]
                with open(f'Done.csv' , 'a', encoding='utf8') as done:
                        writer = csv.writer(done)
                        writer.writerow(cool)
        r=""        
def tagall(tag,api):
    for page in range(1,501):
        r = requests.get(f'https://openapi.etsy.com/v2/listings/active?tags={tag}&limit=100&page={page}&api_key={api}').text
        time.sleep(0.5)
        data = json.loads(r)
        for i in data['results']:

                title = i['title']
                creation = i.get('original_creation_tsz')
                date = str(pd.to_datetime(datetime.today()).date() - pd.to_datetime(datetime.fromtimestamp(creation)).date())
                days=date[ok]
                price = i.get('price')
                quantity = i.get('quantity')
                views = i.get('views')
                num_favorers = i.get('num_favorers')
                url = i.get('url')
                                
                cool = [views,num_favorers,days,quantity,price,title,url]
                with open(f'Done.csv' , 'a', encoding='utf8') as done:
                        writer = csv.writer(done)
                        writer.writerow(cool)
        r=""     
def keywordTagdigital(keyword,tag,api):
    for page in range(1,501):
        r = requests.get(f'https://openapi.etsy.com/v2/listings/active?keywords={keyword}&tags={tag}&is_digital=1&limit=100&page={page}&api_key={api}').text
        time.sleep(0.5)
        data = json.loads(r)
        for i in data['results']:

                title = i['title']
                creation = i.get('original_creation_tsz')
                date = str(pd.to_datetime(datetime.today()).date() - pd.to_datetime(datetime.fromtimestamp(creation)).date())
                days=date[ok]
                price = i.get('price')
                quantity = i.get('quantity')
                views = i.get('views')
                num_favorers = i.get('num_favorers')
                url = i.get('url')
                                
                cool = [views,num_favorers,days,quantity,price,title,url]
                with open(f'Done.csv' , 'a', encoding='utf8') as done:
                        writer = csv.writer(done)
                        writer.writerow(cool)
        r="" 
def keywordTagall(keyword,tag,api):
    for page in range(1,501):
        r = requests.get(f'https://openapi.etsy.com/v2/listings/active?keywords={keyword}&tags={tag}&limit=100&page={page}&api_key={api}').text
        time.sleep(0.5)
        data = json.loads(r)
        for i in data['results']:

                title = i['title']
                creation = i.get('original_creation_tsz')
                date = str(pd.to_datetime(datetime.today()).date() - pd.to_datetime(datetime.fromtimestamp(creation)).date())
                days=date[ok]
                price = i.get('price')
                quantity = i.get('quantity')
                views = i.get('views')
                num_favorers = i.get('num_favorers')
                url = i.get('url')
                                
                cool = [views,num_favorers,days,quantity,price,title,url]
                with open(f'Done.csv' , 'a', encoding='utf8') as done:
                        writer = csv.writer(done)
                        writer.writerow(cool)
        r="" 
if method_search == "1":
    if all_or_no == "1":
        keyword=input("Enter Keyword : ")
        keywordall(keyword,api)
    elif all_or_no == "2":
        keyword=input("Enter Keyword : ")
        keyword_digital(keyword,api)
elif method_search == "2":
    if all_or_no == "1":
        tag=input("Enter Tag : ")
        tagall(tag,api)
    elif all_or_no == "2":
        tag=input("Enter Tag : ")
        tagdigital(tag,api)
elif method_search == "3":
        if all_or_no == "1":
            keyword=input("Enter Keyword : ")
            tag=input("Enter Tag : ")
            keywordTagall(keyword,tag,api)
        elif all_or_no == "2":
            keyword=input("Enter Keyword : ")
            tag=input("Enter Tag : ")
            keywordTagdigital(keyword,tag,api)


print("DONE!!")
