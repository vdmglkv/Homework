![python logo](RP/templates/Python_logo.jpg) 
# Author
Vadim Gulakov

---

# Description
CLI:

This rss_reader cli use for:

- parse rss page and display information in json or human-readable formats.

- keep rss news in local cache(Database SQLite3).

- convert news into pdf or html format.

---
# Requirements
- Python>=3.9

---

# Installations
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


# Parser without installations

In repo:
>python rss_parser.py [options]
---
# Usage
CLI:

```
$ rss_reader --help
usage: rss_reader [-h] [--version] [--json] [--html FILE] [--pdf FILE]
                  [--verbose] [--limit LIMIT] [--date DATE]
                  [--clear]
                  source
                  
Pure Python command-line RSS reader.

positional arguments:
  source          RSS URL

optional arguments:
  -h, --help      show this help message
  --version       Print version info
  --json          Print result as JSON in stdout
  --html FILE  Convert rss feed into html and save as file
  --pdf FILE   Convert rss feed into pdf and save as file
  --verbose       Outputs verbose status messages
  --limit LIMIT   Limit news topics if this parameter provided
  --date DATE     Extract news from cache. Take a start publish date in
                  format YYYYMMDD
  --clear         Clear news cache
```
# Example:


> rss_reader (in default case parse https://news.yahoo.com/rss/) 
```
Feed: Yahoo News - Latest News & Headlines
=================================================================================================================================================================================
Title: Cheap antidepressant shows promise treating early COVID-19
Data: 2021-10-27T22:37:35Z
Link: https://news.yahoo.com/cheap-antidepressant-shows-promise-treating-223735055.html

Text:
A cheap antidepressant reduced the need for hospitalization among high-risk adults with COVID-19 in a study hunting for existing drugs that could be repurposed to treat coronavirus.
Researchers tested the pill used for depression and obsessive-compulsive disorder because it was known to reduce inflammation and looked promising in smaller studies.
They've shared the results with the U.S. National Institutes of Health, which publishes treatment guidelines, and they hope for a World Health Organization recommendation.
“If WHO recommends this, you will see it widely taken up,” said study co-author Dr. Edward Mills of McMaster University in Hamilton, Ontario, adding that many poor nations have the dru
g readily available. “We hope it will lead to a lot of lives saved.”
The pill, called fluvoxamine, would cost $4 for a course of COVID-19 treatment. By comparison, antibody IV treatments cost about $2,000 and Merck's experimental antiviral pill for COVI
D-19 is about $700 per course. Some experts predict various treatments eventually will be used in combination to fight the coronavirus.

Image: https://s.yimg.com/uu/api/res/1.2/4XvMxiuN0axashY4vvuQLw--~B/aD0xNjA4O3c9MjUxMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/4168c825dd9423c04fb059c73db62fd8
```
> rss_parser --json
```
Feed: Yahoo News - Latest News & Headlines
{'link': 'https://news.yahoo.com/cheap-antidepressant-shows-promise-treating-223735055.html',
 'published': '2021-10-27T22:37:35Z',
 'text': 'A cheap antidepressant reduced the need for hospitalization among '
         'high-risk adults with COVID-19 in a study hunting for existing drugs '
         'that could be repurposed to treat coronavirus.\n'
         'Researchers tested the pill used for depression and '
         'obsessive-compulsive disorder because it was known to reduce '
         'inflammation and looked promising in smaller studies.\n'
         "They've shared the results with the U.S. National Institutes of "
         'Health, which publishes treatment guidelines, and they hope for a '
         'World Health Organization recommendation.\n'
         '“If WHO recommends this, you will see it widely taken up,” said '
         'study co-author Dr. Edward Mills of McMaster University in Hamilton, '
         'Ontario, adding that many poor nations have the drug readily '
         'available. “We hope it will lead to a lot of lives saved.”\n'
         'The pill, called fluvoxamine, would cost $4 for a course of COVID-19 '
         'treatment. By comparison, antibody IV treatments cost about $2,000 '
         "and Merck's experimental antiviral pill for COVID-19 is about $700 "
         'per course. Some experts predict various treatments eventually will '
         'be used in combination to fight the coronavirus.\n',
 'title': 'Cheap antidepressant shows promise treating early COVID-19',
 'url': 'https://s.yimg.com/uu/api/res/1.2/4XvMxiuN0axashY4vvuQLw--~B/aD0xNjA4O3c9MjUxMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/4168c825dd9423c04fb059c73db62fd8'}
```
> rss_parser --date 20211027
```
[INFO] Loaded news from cache:
Channel: Yahoo News - Latest News & Headlines
Link: https://news.yahoo.com/rss/
Title: Cheap antidepressant shows promise treating early COVID-19
News link: https://news.yahoo.com/cheap-antidepressant-shows-promise-treating-223735055.html
Date: 2021-10-27T22:37:35Z
Image: https://s.yimg.com/uu/api/res/1.2/4XvMxiuN0axashY4vvuQLw--~B/aD0xNjA4O3c9MjUxMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/4168c825dd9423c04fb059c73db62fd8
```

