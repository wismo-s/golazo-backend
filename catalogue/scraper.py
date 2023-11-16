from bs4 import BeautifulSoup
import requests as resq
#class_="lazyloaded"

def catalogScraper(url, html_class, includ):
    URL_BASE = f'https://www.alphafit.pe/collections/{url}'
    obtain_request = resq.get(URL_BASE)
    html_result = obtain_request.text 
    soup = BeautifulSoup(html_result, "html.parser")
    images_divs = soup.find_all('img', class_=f'{html_class}')
    api_content = []
    count = 0
    for img in images_divs:
         if f'{includ}' in img['alt']:
            src = img['src'].split("//")[1]
            obj = { 'id': count, 'title': img['alt'], 'img': src}
            count+=1
            api_content.append(obj)
    return api_content