"# Web Scraping with Beautiful Soup

 "## Working with objects

! pip install BeautifulSoup
 
from bs4 import BeautifulSoup
 
 html_doc = '''
  <html><head><title>Best Books</title></head>
 <body>
<p class='title'><b>DATA SCIENCE FOR DUMMIES</b></p>

<p class='description'>Jobs in data science abound, but few people have the data science skills needed to fill these increasingly important roles in organizations. Data Science For Dummies is the pe
<br><br>
Edition 1 of this book:
         <br>
<ul>
 <li>Provides a background in data science fundamentals before moving on to working with relational databases and unstructured data and preparing your data for analysis</li>
 <li>Details different data visualization techniques that can be used to showcase and summarize your data</li>
 <li>Explains both supervised and unsupervised machine learning, including regression, model validation, and clustering techniques</li>
 <li>Includes coverage of big data processing tools like MapReduce, Hadoop, Storm, and Spark</li>   
  </ul>
<br><br>
"What to do next:
<br>
<a href='http://www.data-mania.com/blog/books-by-lillian-pierson/' class = 'preview' id='link 1'>See a preview of the book</a>,
<a href='http://www.data-mania.com/blog/data-science-for-dummies-answers-what-is-data-science/' class = 'preview' id='link 2'>get the free pdf download,</a> and then
<a href='http://bit.ly/Data-Science-For-Dummies' class = 'preview' id='link 3'>buy the book!</a> 
</p>

<p class='description'>...</p>
    '''
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup)

# adds some structure
print soup.prettify()[0:350]

"### Tag objects
 
"#### Working with names"
soup = BeautifulSoup('<b body=\"description\"\">Product Description</b>', 'html')

# creates a tag called "b"
tag=soup.b
type(tag)
print tag
 tag.name

# replaces tag's name "b" with "bestbooks"
tag.name = 'bestbooks'
tag
tag.name
  
 "#### Working with attributes"
tag['body']
tag.attrs

tag['id'] = 3
tag.attrs

tag

# deletes an attribute
del tag['body']
del tag['id']
tag

 tag.attrs
  
 "#### Using tags to navigate a tree
# 1. recreate the parse tree
html_doc = '''
 <html><head><title>Best Books</title></head>
<body>
<p class='title'><b>DATA SCIENCE FOR DUMMIES</b></p>

<p class='description'>Jobs in data science abound, but few people have the data science skills needed to fill these increasingly important roles in organizations. Data Science For Dummies is the pe
<br><br>
Edition 1 of this book:
        <br>
 <ul>
  <li>Provides a background in data science fundamentals before moving on to working with relational databases and unstructured data and preparing your data for analysis</li>
  <li>Details different data visualization techniques that can be used to showcase and summarize your data</li>
  <li>Explains both supervised and unsupervised machine learning, including regression, model validation, and clustering techniques</li>
  <li>Includes coverage of big data processing tools like MapReduce, Hadoop, Storm, and Spark</li>   
  </ul>
<br><br>
What to do next:
<br>
<a href='http://www.data-mania.com/blog/books-by-lillian-pierson/' class = 'preview' id='link 1'>See a preview of the book</a>,
<a href='http://www.data-mania.com/blog/data-science-for-dummies-answers-what-is-data-science/' class = 'preview' id='link 2'>get the free pdf download,</a> and then
<a href='http://bit.ly/Data-Science-For-Dummies' class = 'preview' id='link 3'>buy the book!</a> 
</p>

<p class='description'>...</p>
'''
soup = BeautifulSoup(html_doc, 'html.parser')
 
soup.head

soup.title

soup.body.b
 
soup.body
 # unordered list
soup.ul

soup.a

"## Exploring NavigableString Objects"

from bs4 import BeautifulSoup

"### The BeautifulSoup object"

soup = BeautifulSoup('<b body=\"description\">Product description</b>')

"### NavigableString objects
 tag= soup.b
 type(tag)

tag.name
 tag.string
type(tag.string)
 
nav_string = tag.string
nav_string
 
 # replace
nav_string.replace_with('Null')
tag.string
 
"#### Working with NavigableString objects
 
html_doc = '''
<html><head><title>Best Books</title></head>
<body>
<p class='title'><b>DATA SCIENCE FOR DUMMIES</b></p>

<p class='description'>Jobs in data science abound, but few people have the data science skills needed to fill these increasingly important roles in organizations. Data Science For Dummies is the pe
<br><br>
Edition 1 of this book:
        <br>
 <ul>
  <li>Provides a background in data science fundamentals before moving on to working with relational databases and unstructured data and preparing your data for analysis</li>
  <li>Details different data visualization techniques that can be used to showcase and summarize your data</li>
  <li>Explains both supervised and unsupervised machine learning, including regression, model validation, and clustering techniques</li>
  <li>Includes coverage of big data processing tools like MapReduce, Hadoop, Storm, and Spark</li>   
  </ul>
<br><br>
What to do next:
<br>
<a href='http://www.data-mania.com/blog/books-by-lillian-pierson/' class = 'preview' id='link 1'>See a preview of the book</a>,
<a href='http://www.data-mania.com/blog/data-science-for-dummies-answers-what-is-data-science/' class = 'preview' id='link 2'>get the free pdf download,</a> and then
<a href='http://bit.ly/Data-Science-For-Dummies' class = 'preview' id='link 3'>buy the book!</a> 
</p>

<p class='description'>...</p>
'''
soup = BeautifulSoup(html_doc, 'html.parser')

for string in soup.stripped_strings: print(repr(string))
 
title_tag = soup.title
title_tag
title_tag.parent
title_tag.string
title_tag.string.parent

"## Data parsing
import pandas as pd
from bs4 import BeautifulSoup
import re   #regex

r = '''
<html><head><title>Best Books</title></head>
<body>
<p class='title'><b>DATA SCIENCE FOR DUMMIES</b></p>

<p class='description'>Jobs in data science abound, but few people have the data science skills needed to fill these increasingly important roles in organizations. Data Science For Dummies is the pe,
<br><br>
Edition 1 of this book:
        <br>
 <ul>
  <li>Provides a background in data science fundamentals before moving on to working with relational databases and unstructured data and preparing your data for analysis</li>,
  <li>Details different data visualization techniques that can be used to showcase and summarize your data</li>,
  <li>Explains both supervised and unsupervised machine learning, including regression, model validation, and clustering techniques</li>,
  <li>Includes coverage of big data processing tools like MapReduce, Hadoop, Storm, and Spark</li>   ,
  </ul>
<br><br>
What to do next:
<br>
<a href='http://www.data-mania.com/blog/books-by-lillian-pierson/' class = 'preview' id='link 1'>See a preview of the book</a>,,
<a href='http://www.data-mania.com/blog/data-science-for-dummies-answers-what-is-data-science/' class = 'preview' id='link 2'>get the free pdf download,</a> and then,
<a href='http://bit.ly/Data-Science-For-Dummies' class = 'preview' id='link 3'>buy the book!</a> ,
</p>

<p class='description'>...</p>,
'''"
 
soup = BeautifulSoup(r, 'lxml')
type(soup)
 
### Parsing your data
  
print soup.prettify()[0:100]
 
### Getting data from a parse tree

text_only = soup.get_text()
print(text_only)
 
### Searching and retrieving data from a parse tree,

#### Retrieving tags by filtering with name arguments"
 
soup.find_all(\"li\")

#### Retrieving tags by filtering with keyword arguments"
 
soup.find_all(id=\"link 3\")
 
##### Retrieving tags by filtering with string arguments
soup.find_all('ul')

#### Retrieving tags by filtering with list objects
 soup.find_all(['ul', 'b'])
 
#### Retrieving tags by filtering with regular expressions
l = re.compile('l')

for tag in soup.find_all(l): print(tag.name)
 
#### Retrieving tags by filtering with a Boolean value"

for tag in soup.find_all(True): print(tag.name)
 
#### Retrieving weblinks by filtering with string objects

for link in soup.find_all('a'): print(link.get('href'))
 
#### Retrieving strings by filtering with regular expressions

soup.find_all(string=re.compile(\"data\"))
 

"## Web scraping
 
from bs4 import BeautifulSoup
import urllib
import re

r = urllib.urlopen('https://analytics.usa.gov').read()
soup = BeautifulSoup(r, "lxml")
type(soup)

### Scraping a webpage and saving your results"
  
print soup.prettify()[:100]

for link in soup.find_all('a'): print(link.get('href'))
 
for link in soup.findAll('a', attrs={'href': re.compile("^http")}): print link
 
file = open('parsed_data.txt', 'wb')
for link in soup.findAll('a', attrs={'href': re.compile("^http")}):
    soup_link = str(link)
    print soup_link
    file.write(soup_link)
file.flush()
file.close()
 # to find where the file was saved
%pwd




