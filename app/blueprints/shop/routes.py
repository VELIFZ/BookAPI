# Making api call to sell api that is created wirh sell form. 
from flask import Blueprint, render_template, request, url_for
import requests as r
from app.models import db, User, Book

shop = Blueprint('shop', __name__, template_folder='shop_templates', url_prefix = '/shop') 

# @shop.route('/buy')
# def buy():
#     res = r.get('https://the-book-cafe.herokuapp.com/api/books').json()
#     if res:
#         try:
#             book = res["Books"]
#             return render_template('buy.html', book=book)    
#         except:
#             return ''
#     return render_template('buy.html')

@shop.route('/buy')
def buy():
    #page = request.args.get('page', 1, type=int)
    all_books = Book.query.order_by(Book.date_posted.desc()).all()
    return render_template('buy.html', all_books=all_books)


@shop.route('/<string:id>')
def single_page(id):
    single_book = Book.query.get(id)
    return render_template('single_page.html', single_book=single_book)

@shop.route('/cart')
def addcart():
    return render_template('cart.html')