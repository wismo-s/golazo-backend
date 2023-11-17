from bs4 import BeautifulSoup
import requests as resq

def catalogScraper(url, html_class, includ):
    URL_BASE = f'https://www.alphafit.pe/collections/{url}'
    obtain_request = resq.get(URL_BASE)
    html_result = obtain_request.text 
    soup = BeautifulSoup(html_result, "html.parser")
    images_divs = soup.find_all('img', class_=f'{html_class}')
    price_str = soup.find_all('div', class_='grid-product__price')
    api_content = []
    for i in range(0, len(images_divs)):
        image = images_divs[i]
        price = price_str[i].get_text(strip=True).split(" ")[-1]
        if f'{includ}' in image['alt']:
            src = image['src'].split("//")[1]
            obj = {'id': i, 'name': image['alt'], 'img': src, 'price': price}
            api_content.append(obj)
            """
            serialiser = ProductSerilizer(data=obj)
            if serialiser.is_valid():
                serialiser.save()
            """
    return api_content