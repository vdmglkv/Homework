from bs4 import BeautifulSoup
# from colorama import Fore
import requests


class News:

    def __init__(self, title, link, published):
        self.title = title
        self.link = link
        self.published = published

    def get_info(self):
        print(f'Title: {self.title}')
        print(f'Data: {self.published}')
        print(f'Link: {self.link}')


class ParserRSS:

    def __init__(self, rss_url):

        self.session = requests.Session()
        self.link = rss_url

    def parse(self, tag='item'):

        try:
            response = self.session.get(self.link)
            soup = BeautifulSoup(response.content, features='xml')
            data = soup.findAll(tag)
            return data

        except Exception as e:
            print('[INFO] The scraping job failed. See exception: ')
            print(e)

    def get_page_title(self):
        data = self.parse('channel')
        for inf in data:
            return inf.find('title').text

    def get_news(self):

        articles_list = []
        articles = self.parse()

        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            published = a.find('pubDate').text

            article = {
                'title': title,
                'link': link,
                'published': published
            }
            news = News(**article)
            articles_list.append(news)

        return articles_list


if __name__ == '__main__':
    print('Starting scraping')

    print('Finished scraping')
