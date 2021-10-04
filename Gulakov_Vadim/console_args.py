import argparse

parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader')

parser.add_argument('--version', nargs='?', const='1.4', type=str, help='Print version info')
parser.add_argument('--json', nargs='?', const=False, type=bool, help='Print result as JSON in stdout')
parser.add_argument('--verbose', nargs='?', const=False, type=bool, help='Outputs verbose status messages')
parser.add_argument('--limit', nargs='?', const=1, type=int, help='Limit news topics if this parameter provided')

args = parser.parse_args()
