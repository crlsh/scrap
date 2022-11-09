from bs4 import BeautifulSoup
import requests
import json
import datetime
from os import path
import pymongo
from pymongo import MongoClient 


cluster=MongoClient("mongodb+srv://AdminScrap:HXfk6qDTCyzzqhLw@cluster0.oxitgjo.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Precios"]
collection = db["Super"]
post ={'super': 'carrefour', 'producto': 'Fideos', 'url': 'https://supermercado.laanonimaonline.com/almacen/fideos/largos-y-guiseros/fideos-mostachol-lucchetti-x-500-g/art_11/', 'fecha': '08-11-2022', 'precio': '290'}




collection.insert_one(post)
print ("post insertado")

resultados=collection.find({"super":"carrefour"})
for result in resultados:
     print(result)

