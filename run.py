from app import app
from app.models import db, User # model ekledikce buraya ekle table isimlerini

@app.shell_context_processor
def shell_context():
    return {'db': db, 'User': User} #buraya table isimleri ekle test etmek istedikce 