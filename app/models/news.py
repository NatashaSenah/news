class News:
    def __init__(self,id,name,description,category,country):
        self.id =id
        self.name = name
        self.description=description
        self.category=category
        self.country=country
class Articles:
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author=author 
        self.title = title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt 
