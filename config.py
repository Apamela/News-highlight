import os

class Config:

    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?id={}api_Key={}'
    ARTICLES_BASE_URL='https://newsapi.org/v2/everything?id={}api_Key={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}