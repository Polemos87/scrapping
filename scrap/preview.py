import requests
import bs4

def preview_scrap():
    KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

    response = requests.get('https://habr.com/ru/all/')
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, features='html.parser')

    articles = soup.find_all('article')
    articles_list = []
    for article in articles:
        article_1 = set(article.text.split())
        if KEYWORDS & article_1:
            date_class = 'tm-article-snippet__datetime-published'
            link_class = 'tm-article-snippet__title-link'
            date = article.find(class_=date_class).text
            title = article.find('h2').text
            href = article.find(class_=link_class).attrs['href']
            link = 'https://habr.com/' + href
            article_new = [date, title, link]
            articles_list.append(article_new)
    print('В превью:')
    print(articles_list)
