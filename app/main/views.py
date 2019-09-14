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
    sources= get_sources('sports')
    technology_sources= get_sources('technology')
    business_sources= get_sources('business')
    politics_sources= get_sources('politics')
    title="News-highlight"
    return render_template('index.htm',title=tltle,sources=sources,technology=technology_sources,business=business_sources,politics=politics_sources)

@main.route('/sources/<id>')
def articles(id):
    '''
    view articles page
    '''
    articles= get_articles(id)
    title='top articles'
    return render_template('articles.html',title=title,articles=articles)