from app import app

from flask import redirect, render_template, request, url_for, redirect, flash, session
from .forms import Search
from flask_paginate import Pagination, get_page_parameter


import requests as r


@app.route('/')
def home():
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

