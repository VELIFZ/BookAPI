from app import app

from flask import redirect, render_template, request, url_for, redirect, flash, session
from .forms import Search
from flask_paginate import Pagination, get_page_parameter


import requests as r


@app.route('/', methods = ['GET', 'POST'])
def home():
    res = r.get('https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=c8oaOdaN23MxlZSAstdGA29PJtWu3oFA').json()
    if res:
        try:
            best_s = res["results"]["books"]
            first_i = best_s[0]['book_image']
            return render_template('index.html', best_s=best_s, first_i=first_i)    
        except:
            return ''
    return render_template('index.html')

# making the google book api call - I need items for now which its a list contains dictionaries, every index is containes more dictionaries about single book
@app.route('/search', methods = ['GET', 'POST'])
def search():
    form = Search()
    if request.method == "POST":
        res = r.get(f'https://www.googleapis.com/books/v1/volumes?q={form.name.data}&maxResults=40').json()
        if res:
            try:
                items = res['items']
                # doing pagination after api call
                page = request.args.get('page', 1, type=int)
                pagination = Pagination(page = page, total=len(items), per_page=5)
                return render_template('search.html', form=form, items=items, pagination=pagination)
            except:
                flash(f"Can't find what you're looking for. Try another name.", category='danger')
                return redirect(url_for('search'))
        else:
            return redirect(url_for('search'))
    return render_template('search.html', form=form )

@app.route('/shop')
def shop():
    res = r.get('https://the-book-cafe.herokuapp.com/api/books').json()
    if res:
        try:
            book = res["Books"]
            return render_template('shop.html', book=book)    
        except:
            return ''
    return render_template('shop.html')