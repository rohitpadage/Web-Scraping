from bs4 import BeautifulSoup
import pandas as pd
import requests

url='https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers'
source=requests.get(url)
print(source.text)
soup=BeautifulSoup(source.text,'html.parser')
print(soup)    

best_seller=soup.find_all('div',class_='a-row a-carousel-controls a-carousel-row a-carousel-has-buttons')

txt_lst=[]
for i in best_seller:
        txt_lst.append(i.text)

for i in range(len(txt_lst)):   # remove last unneccesary word
    txt_lst[i]=txt_lst[i][:-9] 

res=[]
for i in range(len(txt_lst)):           # split the '#'
    r=txt_lst[i].split('#')             
    #print(r[1:])
    res.append(r[1:])
print(res)


for i in range(len(res)):               # Remove the number
    for j in range(len(res[i])):
        print(res[i][j][1:])    
        res_lst.append(res[i][j][1:])

data=pd.DataFrame({'Name':res_lst})
data.to_csv('amazon3.csv')

k='a-row a-carousel-header-row a-size-large'

best_seller_title=soup.find_all('div',class_=k)

title_len=len(best_seller_title)

for i in range(title_len):
    best_seller_title[i]=best_seller_title[i].text[:-4

category=[]
for i in best_seller_title:
    for j in range(6):
        category.append(i)
    
data=pd.DataFrame({'Name':res_lst,'Category':category})
data.to_csv('amazon4.csv')






