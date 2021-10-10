from bs4 import BeautifulSoup
from console_args import args
# from colorama import Fore
import requests
import sys

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 '
                  'Safari/537.36 '
}


class News:

    def __init__(self, title: str, link: str, published: str, text: str, url: str):
        self.title = title
        self.link = link
        self.published = published
        self.text = text
        self.url = url

    def get_info(self):
        print(f'Title: {self.title}')
        print(f'Data: {self.published}')
        print(f'Link: {self.link}')
        print()
        print('Text:')
        print(self.text)
        print(f'Image: {self.url}')


class ParserRSS:

    def __init__(self, rss_url: str):

        self.session = requests.Session()
        self.link = rss_url

    def parse(self, link, parser_type: str = 'xml', tag: str = 'item', class_: str = ''):

        try:
            response = self.session.get(link, headers=HEADERS)
            soup = BeautifulSoup(response.content, parser_type)
            data = soup.find_all(tag, attrs={'class': class_})
            return data

        except Exception as e:
            print('[INFO] The scraping job failed. See exception: ')
            print(e)

    def get_news_text(self, link):
        text = ''
        data = self.parse(link, tag='p', parser_type='html.parser')

        for p in data[:3]:
            text += str(p)[3:len(p) - 5] + '\n'

        return text

    def get_page_title(self):
        try:
            data = self.parse(self.link, tag='channel')
            for inf in data:
                return inf.find('title').text
        except TypeError as ex:
            print(f'[INFO] Invalid url!')
            sys.exit()

    def get_news(self):

        articles_list = []
        articles = self.parse(args.source)

        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            published = a.find('pubDate').text
            media_content = str(a.find('media:content')).split('\"')

            text = self.get_news_text(link)

            if 'None' not in media_content:
                url = media_content[3]
                article = {
                    'title': title,
                    'link': link,
                    'published': published,
                    'text': text,
                    'url': url
                }
                news = News(**article)
                articles_list.append(news)
        return articles_list


def main():
    try:

        if args.source is not None:

            if '--version' in sys.argv:
                print(f'[INFO] Version: {args.version}')

            print('[INFO] Starting scraping')
            pars = ParserRSS(args.source)
            print(f'Feed: {pars.get_page_title()}')
            newses = pars.get_news()

            for news in newses[:args.limit]:
                print('=' * 200)
                news.get_info()
                print('=' * 200)

            print('[INFO] Finished scraping')
        elif args.source is None and '--version' in sys.argv:
            print(f'[INFO] Version: {args.version}')
        else:
            print('[INFO] Link input expected!')

    except KeyboardInterrupt:
        print()
        print('[INFO] Stopped by console!')


if __name__ == '__main__':
    main()
