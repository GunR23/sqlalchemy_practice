from database.models.book import Book
from flask import Blueprint, request, redirect, make_response, url_for, jsonify
from utils.logger import logger
from app import session


book_blueprint = Blueprint('books', __name__)


@book_blueprint.route("/")
def show_books():
    books = session.query(Book).all()
    return books


@book_blueprint.route('/books/new/', methods=['GET', 'POST'])
def new_book():
    if request.method == 'POST':
        book_to_add = Book(title=request.form['name'], author=request.form['author'], genre=request.form['genre'])
        session.add(book_to_add)
        session.commit()
        logger.info(f"Added new book to DB: {book_to_add.title} by {book_to_add.author}")
        return redirect(url_for('show_books'))
    else:
        return make_response(jsonify("error"))


@book_blueprint.route('/books/<int:book_id>/edit/', methods=['GET', 'POST'])
def edit_book(book_id):
    edited_book = session.query(Book).filter_by(id=book_id).one()
    if request.method == 'POST':
        if request.form['name']:
            edited_book.title = request.form['name']
            logger.info(f"Edited book: {edited_book.title} by {edited_book.author}")
            return redirect(url_for(show_books))
    else:
        return make_response(jsonify("error"))


@book_blueprint.route('/books/<int:book_id>/delete/', methods=['GET', 'POST'])
def delete_book(book_id):
    book_to_delete = session.query(Book).filter_by(id=book_id).one()
    if request.method == 'POST':
        session.delete(book_to_delete)
        session.commit()
        logger.info(f"Deleted book: {book_to_delete.title} by {book_to_delete.author}")
        return redirect(url_for('showBooks', book_id=book_id))
    else:
        return make_response(jsonify("error"))

