# Making api call to sell api that is created wirh sell form. 
from flask import Blueprint, render_template
import requests as r

shop = Blueprint('shop', __name__, template_folder='shop_templates', url_prefix = '/shop') 

@shop.route('/buy')
def buy():
    res = r.get('https://the-book-cafe.herokuapp.com/api/books').json()
    if res:
        try:
            book = res["Books"]
            return render_template('buy.html', book=book)    
        except:
            return ''
    return render_template('buy.html')

