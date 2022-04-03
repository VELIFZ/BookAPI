from app import app

from flask import redirect, render_template, request, url_for, redirect
from .forms import Search

import requests as r

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods = ['GET', 'POST'])
def search():
    form = Search()
    if request.method == "POST":
        res = r.get(f'https://www.googleapis.com/books/v1/volumes?q={form.name.data}').json()
        if res:
            items = res['items']
            for item in items:
                try:
                    title = item['volumeInfo']['title']
                    published_date = item['volumeInfo']['publishedDate']
                    description = item['volumeInfo']['description']
                    publisher = item['volumeInfo']['publisher']
                    image = item['volumeInfo']['imageLinks']['thumbnail']
                    authors = item['volumeInfo']['authors'][0]
                    categories = item['volumeInfo']['categories'][0]
                except:
                    print('')
                return render_template('search.html', form=form, title=title, authors=authors, published_date=published_date, description=description, publisher=publisher, categories=categories, image=image)
        else:
            return redirect(url_for('search'))
    return render_template('search.html', form=form)
