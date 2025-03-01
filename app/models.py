from . import db

class Standing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pos = db.Column(db.Integer, nullable=False)
    team = db.Column(db.String(100), nullable=False)
    pld = db.Column(db.Integer, nullable=False)
    w = db.Column(db.Integer, nullable=False)
    l = db.Column(db.Integer, nullable=False)
    nr = db.Column(db.Integer, nullable=False)
    pts = db.Column(db.Integer, nullable=False)
    nrr = db.Column(db.Float, nullable=False)
    last_updated = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


        
class Articles:
    '''Define article model'''
    def __init__(self, source, author, title, description, url, urlToImage, publishedAt):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

# Define Contact Model
class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

