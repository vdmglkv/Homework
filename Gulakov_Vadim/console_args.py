import argparse

from parcer import ParserRSS

rss_link = 'https://news.yahoo.com/rss/'

parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader')

parser.add_argument('--version', nargs='?', const='1.4', type=str, help='Print version info')
parser.add_argument('--json', nargs='?', const=False, type=bool, help='Print result as JSON in stdout')
parser.add_argument('--verbose', nargs='?', const=False, type=bool, help='Outputs verbose status messages')
parser.add_argument('--limit', nargs='?', const=1, type=int, help='Limit news topics if this parameter provided')

args = parser.parse_args()
pars = ParserRSS(rss_link)

if __name__ == '__main__':
    print('[INFO] Starting scraping')
    print(pars.get_page_title())
    newses = pars.get_news()
    for news in newses[:args.limit]:
        print('=' * 100)
        news.get_info()
        print('=' * 100)

    print('[INFO] Finished scraping')
