import requests
from bs4 import BeautifulSoup
import json

def scrap_from_url(url):
    reponse=requests.get(url)
    soup=BeautifulSoup(reponse.text,"html.parser")
    # Recupération des div id=item sur l'url
    items=soup.findAll('p')
    # Récuperation de la balise description de la div item
    text=[]
    for i in items:
        text.append(i.text)
    #Suppression des caractères '!?. dans le texte scrappé
    textsplit=[]
    dict=[]
    dictionnaire={}
    characters = "!'?,.-:"
    for i in range(0,len(text)):
        for k in range(len(characters)):
            text[i]=text[i].replace(characters[k]," ")
        # Passage en lower case
        text[i]=text[i].lower()
        # Split de chaque mot de notre texte dans un tableau
        textsplit.append(text[i].split())
    # Création d'un dictionnaire contenant en keys les mots du textes et en values le nombre de fois qu'ils apparaissent
    for phrase in textsplit:
        for word in phrase:
            dict.append(word)
    for word in dict:
        dictionnaire[word]=(dict.count(word)) 
    dictionnaire_sorted={k: v for k, v in sorted(dictionnaire.items(), key=lambda item: item[1],reverse=True)}
    dictionnaire = json.dumps(dictionnaire_sorted)
    return dictionnaire