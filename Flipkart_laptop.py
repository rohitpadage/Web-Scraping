
from bs4 import BeautifulSoup 
import pandas as pd
import requests

txt_lst2=[]
price_lst2=[]

# Making a GET request

for k in range(1,42):
    print(k)
    source = requests.get('https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=',k)
    soup=BeautifulSoup(source.text,'html.parser')
    
    laptop=" "    
    laptop=soup.find_all('div',class_='_4rR01T')
    for i in laptop:
        txt_lst2.append(i.text)
        
    laptop=" " 
    laptop=soup.find_all('div',class_='_30jeq3 _1_WHN1')
    for i in laptop:
        price_lst2.append(i.text[1:])

data=pd.DataFrame({'Model Name':txt_lst2,'Price':price_lst2})
data.to_csv('flipkart7.csv')
