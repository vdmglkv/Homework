import sqlite3 as sql
import os.path
import logging

CACHE = os.path.join(os.path.dirname(__file__), "templates", "rss_cache.db")


def create_table() -> bool:
    try:
        con = sql.connect(CACHE)
        with con:
            cur = con.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS news (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        channel TEXT,
                        title TEXT,
                        link TEXT,
                        pub_date TEXT,
                        search_date DATE,
                        url TEXT UNIQUE);''')
            cur.close()

        con.commit()
        logging.info("SQL table created")
        return True
    except sql.OperationalError:
        logging.error(f"Failed to create cache file in {CACHE}")
        return False


def store_data_in_cache(data: dict):
    try:
        con = sql.connect(CACHE)
        with con:
            cur = con.cursor()
            # cur.execute()
            con.commit()
            cur.close()

    except sql.OperationalError:
        logging.error(f"Failed to store data in cache file {CACHE}")
        return False


def get_data():
    pass


def clear_cache():
    logging.warning(f"User requested to clean cache file '{CACHE}'")
    confirmation = input("Are you sure to clean all data from cache file? "
                         "Press 'y' to confirm or any other key to cancel.\n")
    if confirmation.upper() == 'Y':
        try:
            con = sql.connect(CACHE)
            with con:
                cur = con.cursor()
                cur.execute("DELETE FROM news;")
                con.commit()
                cur.execute("VACUUM;")
                logging.info(f"Delete all data from {CACHE}")

        except sql.OperationalError as ex:
            logging.error(f"Unable to delete data from {CACHE} - {ex}")
    else:
        logging.warning(f"Cleaning cache file '{CACHE}' cancelled")
        print("Cleaning cache file cancelled")
