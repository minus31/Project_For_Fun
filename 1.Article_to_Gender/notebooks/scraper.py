import requests 
from bs4 import BeautifulSoup 
import re 
import datetime
import pandas as pd
def items_links(page):

    res = requests.get(page)
    soup = BeautifulSoup(res.content, "html.parser")

    linkByAges = {}

    for age in [20, 30, 40, 50]:
        item_age = soup.select_one(r".item_age.item_{}s".format(age))
        
        if not item_age:
            continue

        female_links = [item["href"] for item in item_age.select_one('.rank_female').select("a")]
        male_links = [item["href"] for item in item_age.select_one('.rank_male').select("a")]

        linkByAges[age] = [female_links, male_links]

    return linkByAges

def contentsInArticle(link):
    res = requests.get(link)
    soup = BeautifulSoup(res.content, 'html.parser')
    try :
        title = soup.select_one("h3").text.strip()
    except : 
        title = "None"
        
    try: 
        content = soup.select_one("section").text.strip()
    except :
        content = "None"
    
    return title, content

dates = []
title = []
body = []
age_sex = []

start_day = datetime.datetime.now()# - datetime.timedelta(days=113)

for i in range(365): 
    
    date = start_day - datetime.timedelta(days=i)
    date = date.strftime('%Y%m%d')
    
    page = "https://media.daum.net/ranking/age/?regDate={}".format(date)
    
    print("date : {} started".format(date))    
    # Links for the day by ages and sex
    elements = []
    
    linkByAges = items_links(page)
    
    for age in linkByAges.keys():
        
        female = linkByAges[age][0]
        male = linkByAges[age][1]
        
        female_elem = [contentsInArticle(link) for link in female]
        male_elem = [contentsInArticle(link) for link in male]
        
        for fe in female_elem:
            """fe : [title, body]"""
            
            dates.append(date)
            title.append(fe[0])
            body.append(fe[1])
            age_sex.append(str(age) + "&" + "female")
            
            
        for ma in male_elem:
            
            dates.append(date)
            title.append(ma[0])
            body.append(ma[1])
            age_sex.append(str(age) + "&" + "male")

    print("date : {} done \n".format(date))
    
# results = pd.DataFrame(columns=["date", "Title", "Body", "age_sex"])
results = pd.DataFrame({"date": dates, "Title" : title, "Body" : body, "age_sex" : age_sex})
results.tail(10)

import pickle 

with open("./article_202001.bin", "wb") as f :
    
    pickle.dump(results, f)
    
