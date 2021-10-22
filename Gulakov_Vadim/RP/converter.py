from jinja2 import FileSystemLoader, Environment
from console_args import args
import os.path

env = Environment(loader=FileSystemLoader('templates'))


def create_html(path: str, pagetitle: str, newses: list):

    template = env.get_template('base.html')
    path_to_save = os.path.normpath(os.path.join(path, 'newses.html'))
    try:
        with open(path_to_save, 'w', encoding='UTF-8') as file:
            file.write(template.render(page_title=pagetitle, news=newses))
        print(f'Save to {path_to_save}')
    except FileNotFoundError:
        print(f'No such file or directory \'{args.html}\'\n'
              f'Check your path!')


def create_pdf():
    pass
