from app import app

from flask import redirect, render_template, request, url_for, redirect
from .forms import ClassName

import requests as r

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/x', methods = ['GET', 'POST'])
def functionName():
    form = ClassName()
    if request.method == "POST":
        pass
    return render_template('index.html', form=form)