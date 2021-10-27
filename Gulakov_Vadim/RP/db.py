import sqlite3 as sql
import os.path
import logging
from typing import Union

CACHE = os.path.join(os.path.dirname(__file__), "templates", "rss_cache.db")


def create_table() -> bool:
    """
    The method that create local cache and table News in him.

    :return: bool
    """
    try:
        con = sql.connect(CACHE)
        with con:
            cur = con.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS news (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        channel TEXT,
                        source_link TEXT,
                        title TEXT,
                        link TEXT,
                        pub_date TEXT,
                        date DATE,
                        url TEXT UNIQUE);''')
            cur.close()

        con.commit()
        logging.info("SQL table created")
        return True
    except sql.OperationalError:
        logging.error(f"Failed to create cache file in {CACHE}")
        return False


def store_data_in_cache(data: dict, source: str, channel: str) -> bool:
    """
    The method that store news data in local cache.

    :param data: dict
        Dictionary of newses data.

    :param source: str
        Link of source rss feed.

    :param channel: str
        Channel title.

    :return: bool
    """
    try:
        con = sql.connect(CACHE)
        title = data['title']
        link = data['link']
        pubdate = data['published']
        only_date = pubdate.split('T')[0]
        url = data['url']

        with con:
            cur = con.cursor()
            try:
                # cur.execute(f'''INSERT INTO news(channel, title, link, pub_date, search_date, url)
                #                             VALUES({channel}, {title}, {link}, {pubdate}, {search_date}, {url});''')
                cur.execute('''INSERT INTO news(channel, source_link, title, link, pub_date, date, url)
                            VALUES(?, ?, ?, ?, ?, ?, ?);''',
                            (channel, source, title, link, pubdate, only_date, url))
            except sql.IntegrityError:
                cur.execute('''UPDATE news SET 
                            title = ?,
                            pub_date = ?,
                            date = ?,
                            url = ? WHERE
                            link == ? AND (
                            title <> ? OR
                            pub_date <> ? OR
                            url <> ?)''',
                            (title, pubdate, only_date, url, link,
                             title, pubdate, url))
        con.commit()

    except sql.OperationalError:
        logging.error(f"Failed to store data in cache file {CACHE}")
        return False


def get_data(date: str, source: str, limit: int) -> Union[list, None]:
    """
    The method that load newses from local cache.
    :param date: str
        Publish news date
    :param source: str
        Link of source rss feed
    :param limit: int
        Limit news output
    :return: Union[list, None]
    """
    try:
        con = sql.connect(CACHE)
        with con:
            cur = con.cursor()
        if limit is not None:
            cur.execute('''SELECT * FROM news WHERE source_link LIKE ? AND STRFTIME('%Y%m%d', date)=?
                        ORDER BY date DESC LIMIT ?;''', (source, date, limit))
        else:
            cur.execute('''SELECT * FROM news WHERE source_link LIKE ? AND STRFTIME('%Y%m%d', date)=?
                        ORDER BY date DESC;''', (source, date))

        newses = []
        n = 0
        logging.info("Starting retrieval of data from cache file")
        for row in cur:
            n += 1
            logging.info(f"Processing news item #{n}")
            news_dict = {"Channel": row[1],
                         "Channel URL": row[2],
                         "Title": row[3],
                         "Link": row[4],
                         "Date": row[5],
                         "Image": row[7],
                         }
            newses.append(news_dict)
            logging.info(f"News item #{n} added to dictionary")
        con.close()
        if newses:
            if limit is not None and len(newses) < limit:
                logging.warning(f"Limit set to {limit} but only {len(newses)} news found in cache")
            logging.info(f"{len(newses)} news retrieved from cache")
            return newses
        else:
            logging.error(f"No information found in cache for {date}")
            return None

    except sql.OperationalError as err:
        logging.error(f"Unable to retrieve info from cache file '{CACHE}' - {err}")


def clear_cache() -> None:
    """
    The method that clear data from local cache.

    :return: None
    """
    logging.warning(f"User requested to clean cache file '{CACHE}'")
    confirmation = input("Are you sure to clean all data from cache? "
                         "Press 'y' to confirm or any other key to cancel.\n")
    if confirmation.upper() == 'Y':
        try:
            con = sql.connect(CACHE)
            with con:
                cur = con.cursor()
                cur.execute("DROP TABLE news;")
                con.commit()
                logging.info(f"Delete all data from {CACHE}")

        except sql.OperationalError as ex:
            logging.error(f"Unable to delete data from {CACHE} - {ex}")
    else:
        logging.warning(f"Cleaning cache file '{CACHE}' cancelled!")
        print("Cleaning cache file cancelled!")
