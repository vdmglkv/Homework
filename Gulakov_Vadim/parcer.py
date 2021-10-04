from bs4 import BeautifulSoup
# from colorama import Fore
from console_args import args
import requests

rss_link = 'https://news.yahoo.com/rss/'


class ParserRSS:

    def __init__(self):
        self.link = rss_link
        self.version = args.version
        self.json = args.json
        self.verbose = args.verbose
        self.limit = args.limit

    def parser(self, url):

        s = requests.Session()
        articles_list = []
        try:
            response = s.get(url)
            soup = BeautifulSoup(response.content, features='xml')
            articles = soup.findAll('item')

            for a in articles:
                title = a.find('title').text
                link = a.find('link').text
                published = a.find('pubDate').text

                article = {
                    'title': title,
                    'link': link,
                    'published': published
                }
                articles_list.append(article)

            return articles_list

        except Exception as e:
            print('[INFO] The scraping job failed. See exception: ')
            print(e)


print('Starting scraping')
pars = ParserRSS().parser(rss_link)
print('Finished scraping')
