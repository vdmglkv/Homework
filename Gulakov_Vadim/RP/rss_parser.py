import json
from pprint import pprint
from bs4 import BeautifulSoup
from bs4.element import ResultSet
from converter import create_html, create_pdf
from console_args import args
import logging
import RP
import requests
import re
import sys

logger = logging.getLogger(__name__)

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

    def parse(self, link, parser_type: str = 'xml', tag: str = 'item', class_: str = '') -> ResultSet:

        try:
            response = self.session.get(link, headers=HEADERS)
            soup = BeautifulSoup(response.content, parser_type)
            data = soup.find_all(tag, attrs={'class': class_})
            return data

        except Exception as e:
            print('[INFO] The scraping job failed. See exception: ')
            logging.error(e)
            print(e)

    @staticmethod
    def delete_html_tags_from_string(string: str) -> str:
        pattern = r'<[^>]+>|<[^>]+'
        string = re.sub(pattern, '', string)
        return string

    def get_news_text(self, link: str) -> str:
        text = ''
        data = self.parse(link, tag='p', parser_type='html.parser')

        for p in data[:3]:
            text += str(p) + '\n'

        return self.delete_html_tags_from_string(text)

    def get_news(self) -> list:
        try:

            articles_list = []
            articles = self.parse(args.source)

            if args.limit > len(articles):
                args.limit = len(articles)

            try:
                for a in articles[:args.limit]:
                    title = a.find('title').text
                    link = a.find('link').text
                    published = a.find('pubDate').text
                    media = re.findall(r'media:.[^ ]+', str(a))[0]
                    try:
                        url = a.find(media)['url']
                    except KeyError:
                        url = None

                    text = self.get_news_text(link)
                    article = {
                        'title': title,
                        'link': link,
                        'published': published,
                        'text': text,
                        'url': url
                    }
                    articles_list.append(article)
                    # if args.json:
                    #     json_format.append(json.dumps(article))
                    # else:
                    #     news = News(**article)
                    #     articles_list.append(news)
            except KeyError as e:
                logging.error(e)

            return articles_list
        except TypeError as e:
            print(e)
            logging.error(e)
            sys.exit()

    def get_page_title(self) -> str:
        try:
            data = self.parse(self.link, tag='channel')
            for inf in data:
                return inf.find('title').text
        except TypeError as e:
            logging.error(e)
            print(f'[INFO] Invalid url!')
            sys.exit()


def main():
    if args.limit <= 0:
        args.limit = 1

    if args.version:
        print(f'Version: {RP.__version__}')

    try:

        if args.source is not None:

            if args.verbose:
                logging.basicConfig(level=logging.INFO,
                                    format='[%(asctime)s | %(levelname)s]: %(message)s',
                                    datefmt='%m.%d.%Y %H:%M:%S')
            logging.info('Program started')
            pars = ParserRSS(args.source)
            newses = pars.get_news()
            title = pars.get_page_title()
            logging.info('Get page title')
            print(f'Feed: {title}')

            if args.html:
                logging.info('Creating html document with newses...')
                newses_ = [News(**art) for art in newses]
                try:
                    create_html(args.html, title, newses_)
                except Exception as ex:
                    logging.error(ex)
                    print(ex)
                if not args.pdf:
                    sys.exit()

            if args.pdf:
                logging.info('Creating pdf document with newses...')
                newses_ = [News(**art) for art in newses]
                try:
                    create_pdf(args.pdf, title, newses_)
                except Exception as ex:
                    logging.error(ex)
                    print(ex)
                if not args.json:
                    sys.exit()

            if args.json:
                logging.info('Return news in json format')
                for news in newses:
                    news_ = json.dumps(news)
                    pprint(json.loads(news_))
                sys.exit()
            for news in newses:
                news_ = News(**news)
                logging.info('Print news')
                print('=' * 200)
                news_.get_info()

            print('[INFO] Finished scraping')
            logging.info('Program finished')
            logging.debug("Program finished")
        elif args.source is None and not args.version:
            print('[INFO] Link input expected!')

    except KeyboardInterrupt as e:
        logging.error(e)
        print()
        print('[INFO] Stopped by console!')


if __name__ == '__main__':
    main()
