import requests
from bs4 import BeautifulSoup

url="https://www.bbc.com" #URL of the page with the table
response = requests.get(url)

soup=BeautifulSoup(response.text,"html.parser")

#Finding the content based on tags
h1_tags=soup.find_all("h1")
h2_tags=soup.find_all("h2")
p_tags=soup.find_all("p")

#Printing the extracted data
for tag in h1_tags:
    print(tag.text)

for tag in h2_tags:
    print(tag.text)
    
for tag in p_tags:
    print(tag.text)
     