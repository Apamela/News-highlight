class Sources:
    '''
    sources class to define Sources Objects
    '''
    def __init__(self,id,name,description,url,category,country):
        self.id = id
        self.name = name
        self.description= description
        self.url= url
        self.category= category
        self.country= country
class Articles:
    '''
    Articles class to define articles objects
    '''
    
    def __init__(self,id,author,title,description,url,image,date):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.image = image
        self.url = url
        