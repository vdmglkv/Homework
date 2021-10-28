#Author
Vadim Gulakov

---

#Description
CLI:

This rss_reader cli use for:

- parse rss page and display information in json or human-readable formats.

- keep rss news in local cache(Database SQLite3).

- convert news into pdf or html format.

---
#Requirements
- Python>=3.9

---

#Installations
CLI:

- Clone the repo

>git clone https://github.com/vdmglkv/Homework.git -b finaltask

- In the directory **with setup.py**

Windows
>python setup.py install

Linux/MacOS

>python3 setup.py install

And now you can use CLI:
>rss_parser [options]


#Parser without installations

In repo:
>python rss_parser.py [options]
---
#Usage
CLI:

'''
$ rss_reader --help
usage: rss_reader [-h] [--version] [--json] [--to-html FILE] [--to-pdf FILE]
                  [--verbose] [--limit LIMIT] [--date DATE] [--colorize]
                  [--clear]
                  source

Pure Python command-line RSS reader.

positional arguments:
  source          RSS URL

optional arguments:
  -h, --help      show this help message and exit
  --version       Print version info
  --json          Print result as JSON in stdout
  --html FILE  Convert rss feed into html and save as file
  --pdf FILE   Convert rss feed into pdf and save as file
  --verbose       Outputs verbose status messages
  --limit LIMIT   Limit news topics if this parameter provided
  --date DATE     Extract news from archive. Take a start publish date in
                  format YYYYMMDD
  --clear         Clear news archive
'''

