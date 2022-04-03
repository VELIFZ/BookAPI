# initial blueprint setup
from flask import Blueprint, jsonify, request, redirect, url_for, flash, render_template
from app.blueprints.api.api_forms import SellForm
from flask_login import login_required

api = Blueprint('api', __name__, template_folder='api_templates', url_prefix = '/api') 

# imports for api routes
from app.models import db, Book
from .services import token_required


# Getting book data from user input
@api.route('/sell', methods=['GET', 'POST'])
@login_required
def sell():
    sellform = SellForm()
    if request.method == 'POST':
        if sellform.validate_on_submit():
            # good form info
            sellform = request.form
            new_book = Book(sellform)
            db.session.add(new_book)
            db.session.commit()
            # successful - then take them to their profile 
            #but for now to home page 
            return redirect(url_for('home'))        
        else:
            # bad form info - tell them to try again
            flash('Please fill out required fields.', category='danger')
            return redirect(url_for('api.sell'))
    return render_template('sell.html', sellform=sellform)

# route for getting all books
@api.route('/books', methods=['GET'])
def getBooks():
    """
    [GET] return json data on all of the books in database
    """
    # query the books
    # Jsonifying the result of .to_dict() for each book in our books query
    books = {'Books': [b.to_dict() for b in Book.query.all()]}
    # jsonify and send
    return jsonify(books), 200

# route for getting one book - dynamic route
# the function for this route will expect input coming through the url
@api.route('/book/title/<string:title>', methods=['GET'])
def getBook(title):
    """
    [GET] that accepts an book name through the url and either gets the appropriate book from our database
    or returns that we don't have that book
    """
    b = Book.query.filter_by(title=title.title()).first()
    if b:
        return jsonify(b.to_dict()), 200
    else:
        return jsonify({'Request failed': 'No book with that name.'}), 404

# route for creating a new book
@api.route('/create/book', methods=['POST'])
@token_required
def createBook():
    """
    [POST] creates a new book in our database with data provided in the request body
    expected data format: JSON:
    """
    # grab any json data from the body of the request made to this route
    # depending on how specific we want our data to be - we may want to build out some checks on the data coming in
    # does it actually make sense? is it something we want in our database?
    # otherwise, create the new book in the database
    try:
        data = request.get_json()
        new_book = Book(data)
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'Created New Book': new_book.to_dict()}), 201
    except:
        return jsonify({'Create Book Rejected'}), 400

# route for updating an book
@api.route('/book/update/<string:id>', methods=['PUT']) # PUT is used for updating existing data - just like POST, PUT requests can include data being sent to the web server
@token_required
def updateBook(id):
    """
    [PUT] accepts an book ID in the URL and JSON data in the PUT request body in the following format (all values optional):
    """
    try:
        # grab the request body and query the database for an book with that ID
        book = Book.query.get(id)
        data = request.get_json()
        # then update the book object
        book.from_dict(data)
        # and recommit it to the database aka save changes to the DB
        db.session.commit()
        return jsonify({'Updated book': book.to_dict()}), 200
    except:
        return jsonify({'Request failed': 'invalid body or book ID'}), 400

# route for deleting an book
@api.route('/book/remove/<string:id>', methods=['DELETE'])
@token_required
def removebook(id):
    """
    [DELETE] accepts an book ID - if that ID exists in the database, remove that book from the database
    """
    # check if that book exists
    book = Book.query.get(id)
    if not book: # if no book with that id is in the database
        # tell the user remove failed
        return jsonify({'Remove failed': 'No book of that ID in the database.'}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({'Removed book': book.to_dict()}), 200

@api.route('/stockupdate', methods=['POST'])
def updatestock():
    data = request.get_json()
    for id in data['books']:
        print('id' + id)
        print('quantity' + data['books'][id]['quantity'])
        b = Book.query.get(id)
        b.stock = b.stock - data['books'][id]['quantity']
        if b.stock < 0:
            return jsonify({}), 500
        print(b.to_diict)
    db.session.commit()
    return jsonify({'stock': 'update complete'}), 200
