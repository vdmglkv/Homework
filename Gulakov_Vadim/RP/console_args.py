import argparse
from datetime import datetime
import logging

parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader')

parser.add_argument('source',
                    nargs='?',
                    const='https://news.yahoo.com/rss/',
                    default='https://news.yahoo.com/rss/',
                    type=str,
                    help='RSS URL')
parser.add_argument('--version', nargs='?', const=True, default=False,type=str, help='Print version info')
parser.add_argument("--html", nargs='?', type=str, help="Convert rss feed into html and save as file")
parser.add_argument("--pdf", nargs='?', type=str, help="Convert rss feed into pdf and save as file")
parser.add_argument('--date', nargs='?',  type=str, help='Return newses for that day')
parser.add_argument('--json', nargs='?', const=True, default=False, type=bool, help='Print result as JSON in stdout')
parser.add_argument('--verbose', nargs='?', const=True, default=False, type=bool, help='Outputs verbose status messages')
parser.add_argument('--limit', nargs='?', const=1, default=1, type=int,
                    help='Limit news topics if this parameter provided')

args = parser.parse_args()
