

# Making api call to sell api that is created wirh sell form. 
# from flask import Blueprint, request, redirect, url_for, flash, render_template

# from app.models import Book
# from flask_login import login_required

# shop = Blueprint('shop', __name__, template_folder='shop_templates', url_prefix = '/shop') 

# @shop.route('/shop')
# def shop():
#     page = request.args.get('page',1, type=int)
#     new_items = Book.query.filter(Book.stock > 0).order_by(Book.id.desc()).paginate(page=page, per_page=8)
#     return render_template('shop.html', new_items=new_items)

