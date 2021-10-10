import argparse


parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader')

parser.add_argument('source',
                    nargs='?',
                    const='https://news.yahoo.com/rss/',
                    default='https://news.yahoo.com/rss/',
                    type=str,
                    help='RSS URL')
parser.add_argument('--version', nargs='?', default='1', const='1', type=str, help='Print version info')
parser.add_argument('--json', nargs='?', const=False, type=bool, help='Print result as JSON in stdout')
parser.add_argument('--verbose', nargs='?', const=False, type=bool, help='Outputs verbose status messages')
parser.add_argument('--limit', nargs='?', const=1, default=1, type=int,
                    help='Limit news topics if this parameter provided')

args = parser.parse_args()
