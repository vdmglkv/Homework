import logging
from jinja2 import FileSystemLoader, Environment
from fpdf import FPDF
from console_args import args
import os.path

env = Environment(loader=FileSystemLoader('templates'))


class PDF(FPDF):
    def __init__(self, title: str):
        super().__init__()
        self.title = title

    def header(self):
        w = self.get_string_width(self.title) + 6
        self.set_x((210 - w) / 2)
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        self.set_line_width(1)
        self.cell(w, 9, self.title.replace('?', ''), 1, 1, 'C', 1)
        self.ln(10)

    def footer(self):

        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def set_center_for_string(self, string: str) -> float:
        w = self.get_string_width(string)
        self.set_x((210 - self.get_string_width(string)) / 2)
        self.set_line_width(1)
        self.line(0, self.get_y(), self.w, self.get_y())
        return w


def create_html(path: str, page_title: str, newses: list):

    template = env.get_template('base.html')
    path_to_save = os.path.normpath(os.path.join(path, 'newses.html'))
    try:
        logging.info(f'Try to save in {path_to_save}')
        with open(path_to_save, 'w', encoding='UTF-8') as file:
            file.write(template.render(page_title=page_title, news=newses))
        print(f'Save to {path_to_save}')
    except FileNotFoundError:
        print(f'No such file or directory \'{args.html}\'\n'
              f'Check your path!')


def create_pdf(page_title: str, newses: list, path: str = os.getcwd()):
    font = os.path.join(os.path.dirname(__file__), "templates", "DejaVuSans.ttf")
    pdf = PDF(page_title.encode('latin-1', 'replace').decode('latin-1'))
    pdf.add_font('DejaVu', '', font, uni=True)
    pdf.set_font('DejaVu', '', 12)
    pdf.alias_nb_pages()
    pdf.add_page()

    for i in range(len(newses)):
        title = newses[i].__dict__['title']
        if len(title) > 50:
            title = (title[:50] + '...')
        link = newses[i].__dict__['link']
        text = newses[i].__dict__['text']

        pdf.cell(pdf.set_center_for_string(title), 10, txt='Title: ' + title, ln=1, align='C')

        pdf.cell(pdf.set_center_for_string(link), 10, txt='On site', ln=1, align='C', link=link)

        pdf.cell(pdf.set_center_for_string('News text: '), 10, ln=0, txt="News text: ", align='C')
        pdf.cell(0, 10, ln=1)
        pdf.multi_cell(pdf.w - 10, 10, txt=text, align='L')
        pdf.set_line_width(1)
        pdf.line(0, pdf.get_y(), pdf.w, pdf.get_y())

        if i != len(newses) - 1:
            pdf.add_page()

    path_to_save = os.path.normpath(os.path.join(path, 'newses.pdf'))
    try:
        logging.info(f'Try to save in {path_to_save}')
        pdf.output(path_to_save, 'F')
        print(f'Save to {path_to_save}')
    except FileNotFoundError:
        print(f'No such file or directory \'{args.pdf}\'\n'
              f'Check your path!')
