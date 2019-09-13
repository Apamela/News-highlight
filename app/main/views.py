from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources
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
    title="New-highlight"
    return render_template('index.htm',title=tltle,sources=sources,technology=technology_sources,business=business_sources,politics=politics_sources)
