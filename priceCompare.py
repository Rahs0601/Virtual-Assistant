import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def flipkart():
    url = 'https://flipkart.com/search?q='+str(item)
    r = requests.get(url)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    try:
        link = soup.find("a", {"class": "_2rpwqI"}).attrs['href']
    except:
        pass
    try:
        link = soup.find("a", {"class": "_1fQZEK"}).attrs['href']
    except:
        pass
    try:
        link = soup.find("a", {"class": "_2UzuFa"}).attrs['href']
    except:
        pass
    link = "https://flipkart.com"+str(link)
    r = requests.get(link)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    specifiacaions = soup.find_all('tr', {'class': "_1s_Smc row"})
    print("Specifications")
    for key in specifiacaions:
        print(key.text)
    print("\nFLIPKART:")
    name = soup.find('span', "B_NuCI")
    print("name: ", name.text)
    price = soup.find('div', {'class': '_30jeq3 _16Jk6d'})
    print("price: ", price.text)
    rating = soup.find('div', {'class': '_3LWZlK'})
    print("ratings:", rating.text)
    print("link: ", link)


def amazon():
    url = 'https://www.amazon.in/s?k='+str(item)
    r = requests.get(url, headers=hdr)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    product = soup.find_all(
        "a", {"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})[0]
    link = "https://www.amazon.in"+str(product['href'])
    r = requests.get(link, headers=hdr)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    print("\nAMAZON:")
    name = soup.find('span', "a-size-large product-title-word-break")
    print("name:", name.text)
    price = soup.find('span', {'class': 'a-offscreen'})
    print("price: ", price.text)
    rating = soup.find('span', "a-icon-alt")
    print("ratings:", rating.text)
    print("link: ", link)


def reliance():
    url = 'https://www.reliancedigital.in/search?q='+str(item)
    r = requests.get(url)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    product = soup.find_all('div', class_='sp grid')[0]
    for i in product:
        link = i.get('href')
    link = "https://www.reliancedigital.in"+str(link)
    r = requests.get(link)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    print("\nRELIANCE DIGITAL:")
    name = soup.find('h1', "pdp__title mb__20")
    print("name:", name.text)
    price = soup.find('span', {'class': 'pdp__offerPrice'})
    print("price:", price.text)
    print("link: ", link)


if __name__ == "__main__":
    item = input('enter the product\n')
    ua = UserAgent()
    hdr = {'User-Agent': ua.random,
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    try:
        flipkart()
        amazon()
        reliance()
    except:
        pass