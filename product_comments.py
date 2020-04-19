import requests
from bs4 import BeautifulSoup


def read_n11_comment():

    file_object = open('comments.txt', 'a',encoding='utf8')
    file_object2 = open('links.txt', 'a', encoding='utf8')
    URL = 'https://www.n11.com/arama?q=beta+tea'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml')
    x=soup.find_all("a",attrs={"class":"plink"},href=True)
    for i in x:
        file_object2.write(i["href"])
        URL = i["href"]
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'lxml')
        x=soup.find_all("li")
        #print(soup.title.text)
        #print(soup)
        x=soup.find_all("p")
        z=soup.find_all("li",attrs={"class":"comment"})
        for i in z:
            file_object.write(i.find("p").text)

    file_object.close()
