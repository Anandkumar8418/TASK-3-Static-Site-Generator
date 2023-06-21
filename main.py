from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load

template_environment = Environment(loader=FileSystemLoader(searchpath='./'))
template = template_environment.get_template('html/layout.html')
blogtemplate = template_environment.get_template('html/blogtemplate.html')
tagtemp = template_environment.get_template('html/tagtemplate.html')

with open('article.md') as markdown_file:
    article = markdown(markdown_file.read())
with open('temp.md') as markdown_file:
    articletemp = markdown(markdown_file.read())

with open('tag.md') as markdown_file:
    tagtemple = markdown(markdown_file.read())


with open('config.json') as config_file:
    config = load(config_file)

with open('index.html', 'w') as output_file:
    output_file.write(
        template.render(
            title=config['title'],
            date=config['date'],
            writer=config['writer'],
            tag1=config['tag1'],
            tag2=config['tag2'],
            limks='html/'+config['title']+'.html',
            limk1='html/'+config['tag1']+'.html',
            limk2='html/'+config['tag2']+'.html'

        )
    )
with open('html/'+config['title']+'.html', 'w') as output_file:
    output_file.write(
        blogtemplate.render(
            title=config['title'],
            date=config['date'],
            writer=config['writer'],
            tag1=config['tag1'],
            tag2=config['tag2'],
            article=article,
            limks=config['title']+'.html',
            limk1=config['tag1']+'.html',
            limk2=config['tag2']+'.html'

        ))

with open('html/layout.html', 'w') as output_file:
    output_file.write(
        template.render(
            title=config['title'],
            date=config['date'],
            writer=config['writer'],
            tag1=config['tag1'],
            tag2=config['tag2'],
            nextarticle=articletemp,
            limks='html/'+config['title']+'.html',
            limk1='html/'+config['tag1']+'.html',
            limk2='html/'+config['tag2']+'.html'
        )
    )

try:
    with open('md_support/'+config['tag1']+'count'+'.md'
              ) as markdown_file:
        tagt1count = 1
except FileNotFoundError:
    tagt1count = 0

try:
    with open('md_support/'+config['tag2']+'count'+'.md') as markdown_file:
        tagt2count = 1
except FileNotFoundError:
    tagt2count = 0


if (tagt1count == 0):
    with open('html/'+config['tag1']+'layout'+'.html', 'w') as output_file:
        output_file.write(
            tagtemp.render(

                nexttag=tagtemple
            ))

if (tagt2count == 0):
    with open('html/'+config['tag2']+'layout'+'.html', 'w') as output_file:
        output_file.write(
            tagtemp.render(
                nexttag=tagtemple
            ))

with open('md_support/'+config['tag1']+'count'+'.md','w') as markdown_file:
    markdown_file.write('1')
with open('md_support/'+config['tag2']+'count'+'.md','w') as markdown_file:
    markdown_file.write('1')

tag1temp = template_environment.get_template(
    'html/'+config['tag1']+'layout'+'.html')

tag2temp = template_environment.get_template(
    'html/'+config['tag2']+'layout'+'.html')


with open('html/'+config['tag1']+'.html', 'w') as output_file:
    output_file.write(
        tag1temp.render(
            title=config['title'],
            date=config['date'],
            writer=config['writer'],
            tag1=config['tag1'],
            tag2=config['tag2'],
            limks=config['title']+'.html',
            limk1=config['tag1']+'.html',
            limk2=config['tag2']+'.html'

        ))

with open('html/'+config['tag2']+'.html', 'w') as output_file:
    output_file.write(
        tag2temp.render(
            title=config['title'],
            date=config['date'],
            writer=config['writer'],
            tag1=config['tag1'],
            tag2=config['tag2'],
            limks=config['title']+'.html',
            limk1=config['tag1']+'.html',
            limk2=config['tag2']+'.html'

        ))


with open('html/'+config['tag1']+'layout'+'.html', 'w') as output_file:
    output_file.write(
        tag1temp.render(
            title=config['title'],
            date=config['date'],
            writer=config['writer'],
            tag1=config['tag1'],
            tag2=config['tag2'],
            limks=config['title']+'.html',
            limk1=config['tag1']+'.html',
            limk2=config['tag2']+'.html',
            nexttag=tagtemple
        ))


with open('html/'+config['tag2']+'layout'+'.html', 'w') as output_file:
    output_file.write(
        tag2temp.render(
            title=config['title'],
            date=config['date'],
            writer=config['writer'],
            tag1=config['tag1'],
            tag2=config['tag2'],
            limks=config['title']+'.html',
            limk1=config['tag1']+'.html',
            limk2=config['tag2']+'.html',
            nexttag=tagtemple
        ))
