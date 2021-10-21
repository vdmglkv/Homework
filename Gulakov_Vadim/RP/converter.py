from jinja2 import Template, FileSystemLoader, Environment

env = Environment(loader=FileSystemLoader('templates'))



def create_html(pagetitle, newses):
    template = env.get_template('base.html')
    with open(f'templates/newses.html', 'w', encoding='UTF-8') as file:
        file.write(template.render(page_title=pagetitle, news=newses))

