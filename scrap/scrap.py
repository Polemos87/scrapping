import requests
import bs4


def scrap_full():
    KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

    response = requests.get('https://habr.com/ru/all/')
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, features='html.parser')
    articles = soup.find_all('article')

    link_class = 'tm-article-snippet__title-link'
    date_class = 'tm-article-snippet__datetime-published'
    title_class = 'tm-article-snippet__title tm-article-snippet__title_h2'
    articles_list = []
    for article in articles:
        href = article.find(class_=link_class).attrs['href']
        url = 'https://habr.com' + href
        response = requests.get(url)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, features='html.parser')
        article_1 = soup.find(id='post-content-body')
        article_list = set(article_1.text.split())
        if article_list & KEYWORDS:
            date = article.find(class_=date_class).text
            title = article.find(class_=title_class).text
            article_2 = [f'<{date}> - <{title}> - <{url}>']
            articles_list.append(article_2)
    print('Внутри статей:')
    print(articles_list)

