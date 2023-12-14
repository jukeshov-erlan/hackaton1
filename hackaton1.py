import requests
from bs4 import BeautifulSoup as bs

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data1(html):
    soup = bs(html, 'lxml')
    return soup

def get_data2(soup):
    news = soup.find_all('div', class_='Tag--article')
    count = 0
    data = []

    for new in news:
        try:
            title = new.find('a', class_='ArticleItem--name').text.strip()
            # print(title)
        except:
            title = ''

        try:
            desc_link = new.find('a', class_='ArticleItem--name').get('href')
            # print(link)
        except:
            desc_link = ''

        description_html = get_data1(get_html(desc_link))
        # print(description_html)
        description = description_html.find('div', class_='Article--text').text.replace('\n', '')
        # print(description)

        

        try:
            img = new.find('img').get('src')
            # print(img)
        except:
            img = ''


        data.append([title, img, description])
        count = count + 1
        if count == 20:
            break
    # print(len(data))
    return data

def main():
    url = 'https://kaktus.media/?lable=8&date=2023-09-22&order=time'
    html = get_html(url)
    soup = get_data1(html)
    data = get_data2(soup)
    return data

main()
    