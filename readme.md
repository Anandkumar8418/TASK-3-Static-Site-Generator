# TASK-3-Static-Site-Generator

## Clone this repository to your local folder for using SSG.

## Steps to add your blog - 
1. In config.josn write your Title,tags,date,and name.
```json
{
    "title": "Very important click here",
    "tag1" :"updates",
    "tag2" :"iitk",
    "date" : "21-06-2023",
    "writer" : "Anand Kumar" 
}
```
2. Write your article in article.md as Markdown file
3. To add your blog to index.html now run the main.py file.
4. Host or run index.html to see your blogs there

## Salient Features - 

1.Tags
 - You can click on particular tags to see all blog post with that tag.
  
2.Easily adding blogs.

3.All html files are automatically created by python.



## Use of each file explained - 

1. config.json - It is used to pass title,date,tag etc to python
2. article.md -  It is used to pass the article to be written inside each blog
3. main.py - It combines article.md,config.json and some html templates with some markdown templates.
4. css/main.css - UI done in this file
5. html/ - This folder contains all the html files like layouts,blog pages etc and will contain future blogs once created.
6. tag.md,temp.md - It is for not deleting the previous blogs once new blogs are created by updating the layout. 


## Understanding the Python code - 

### 1.Importing important libraries

```python
from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load
```

### 2. Here taking Layout for index.html and blogs and tags html files.


  Reading from article.md and other md files and config.json
  
```python

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
```

### 3.Creating index.html from layout and then updating layout.html using temp.md

```python
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
```

### 4.Checking if these input tags already exist 

```python
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

```

### 5.If  inputs tags are new then creating new tag html files for these tags

```python
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

```

### 6. Adding content to tag html files

```python
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

```
