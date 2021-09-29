"""Task 4.6 Implement a Pagination class helpful to arrange text on pages and list content on given page. The class
should take in a text and a positive integer which indicate how many symbols will be allowed per each page (take
spaces into account as well). You need to be able to get the amount of whole symbols in text, get a number of pages
that came out and method that accepts the page number and return quantity of symbols on this page. If the provided
number of the page is missing print the warning message "Invalid index. Page is missing". If you're familliar with
using of Excpetions in Python display the error message in this way. Pages indexing starts with 0. }
"""


class Pagination:

    def __init__(self, text, count_of_symbols):
        self.text = text
        self.count_of_symbols = count_of_symbols
        self.items_count = len(text)
        self.pages = [text[i:i + count_of_symbols] for i in range(0, len(text), count_of_symbols)]
        self.page_count = len(self.pages)

    def count_items_on_page(self, page):
        if page >= self.page_count:
            raise Exception('Invalid index. Page is missing.')
        return len(self.pages[page])

    def display_page(self, page):
        return self.pages[page]

    def find_page(self, text_to_find):
        indexsies = []
        for page in self.pages:
            # print(next(iteration) + next(iteration))
            # if self.pages + self.pages == text_to_find:
            #     return self.pages.index(page), self.pages.index(next(page))

            if text_to_find in page:
                indexsies.append(self.pages.index(page))
        return indexsies


a = Pagination('Your beautiful text', 5)
print(a.pages)
print(a.find_page('beaut'))
