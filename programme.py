
## Importation des bibliothèques.
import feedparser as fp
import numpy as np
import json
import newspaper
from newspaper import Article
import pandas as pd
import numpy as np
import csv

nb_articles = 100
list_des_articles = []

data = {}
data['journal'] = {}

# Importer le fichier json contenant les sites web
with open('sites_web.json') as data_file:
    sites_web = json.load(data_file)
    
count = 1
for site_web, value in sites_web.items():
        print("Le site web : ", site_web)
        paper = newspaper.build(value['link'], memoize_articles=False)
        newsPaper = {
            "link": value['link'],
            "articles": []
        }
        noneTypeCount = 0
        for content in paper.articles:
            if count > nb_articles:
                break
            try:
                content.download()
                content.parse()
            except Exception as e:
                print(e)
                print("continuing...")
                continue


            article = {}
            article['title'] = content.title
            article['authors'] = content.authors
            article['text'] = content.text
            article['top_image'] =  content.top_image
            article['movies'] = content.movies
            article['link'] = content.url
            article['published'] = content.publish_date
            newsPaper['articles'].append(article)
            list_des_articles.append(article)
            print(count, "article extrait du ", site_web, " à l'aide de la biblio newspaper, lien: ", content.url)
            count = count + 1
            #noneTypeCount = 0
        count = 1
        data['journal'][site_web] = newsPaper
        
try:
    f = csv.writer(open('les_articles.csv', 'w', encoding='utf-8'))
    f.writerow(['Title', 'Authors','Text','Image','Videos','Link','Published_Date'])
    
    for articl in list_des_articles:
        title = articl['title']
        authors=articl['authors']
        text=articl['text']
        image=articl['top_image']
        video=articl['movies']
        link=articl['link']
        publish_date=articl['published']
        # Ajouter chaque article et son lien associé dans une ligne
        f.writerow([title, authors, text, image, video, link, publish_date])
except Exception as e: print(e)        

