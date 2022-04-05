from app import app
from app.models import db, User, Book, Post # model ekledikce buraya ekle table isimlerini

@app.shell_context_processor
def shell_context():
    return {'db': db, 'User': User, 'Book': Book, 'Post': Post} #buraya table isimleri ekle test etmek istedikce 