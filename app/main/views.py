from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles
from ..models import Sources

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    entertainment= get_sources('entertainment')
    technology= get_sources('technology')
    business= get_sources('business')
    sports= get_sources('sports')
    print('helloooo')
    print(entertainment[0].name)
    title= 'News-highlight'  
    return render_template('index.html',entertainment=entertainment,technology=technology,business=business,sports=sports)

@main.route('/sources/<id>')
def articles(id):
    '''
    view articles page
    '''
    articles= get_articles(id)
    title='top articles'
    return render_template('articles.html',title=title,articles=articles)