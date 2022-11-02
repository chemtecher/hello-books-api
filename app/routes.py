from os import abort
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request, abort

books_bp = Blueprint("books", __name__, url_prefix="/books")



def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message":f"book {book_id} invalid"}, 400))

    book = Book.query.get(book_id)

    if not book:
        abort(make_response({"message":f"book {book_id} not found"}, 404))

    return book

@books_bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book {new_book.title} successfully created", 201)


#Read All books
# @books_bp.route("", methods=["GET"])
# def read_all_books():
#     books_response = []
#     books = Book.query.all()
#     for book in books:
#         books_response.append(
#             {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }
#         )
#     return jsonify(books_response)

@books_bp.route("/<book_id>", methods=["GET"])
def read_one_book(book_id):
    book = validate_book(book_id)
    return {
            "id": book.id,
            "title": book.title,
            "description": book.description
        }

#Updating a Book
@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = validate_book(book_id)

    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(f"Book #{book.id} successfully updated")

#Deleting a Book
@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = validate_book(book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(f"Book #{book.id} successfully deleted")

# Finding a book by title endpoint
# Replaced Read All Books endpoint
@books_bp.route("", methods=["GET"])
def read_all_books():
    # this code replaces the previous query all code
    title_query = request.args.get("title")
    print(title_query)
    if title_query:
        books = Book.query.filter_by(title=title_query)
    else:
        books = Book.query.all()
    # end of the new code

    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })

    return jsonify(books_response)

# #Find One Book without Refactoring
# @books_bp.route("/<book_id>", methods=["GET"]) #postman request => url + /books/3 where 3 == book_id
# def handle_book(book_id):
#     # Handling an invalid book_id
#     try:
#         book_id = int(book_id)
#     except:
#         return {"message":f"book {book_id} invalid"}, 400

#     for book in books:
#         if book.id == book_id:
#             return {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description,
#             }
#     # Handling a non-existing book
#     return {"message":f"book {book_id} not found"}, 404 

# #---------------- Refactoring Finding One Book w/Helper Function ----------------------------------
# #Helper Function using error handling logic 
# def validate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         abort(make_response({"message":f"book {book_id} invalid"}, 400))

#     for book in books:
#         if book.id == book_id:
#             return book

#     abort(make_response({"message":f"book {book_id} not found"}, 404))

# #Updated Find One Book with helper function
# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = validate_book(book_id) #helper function

#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description,
#     }

# @books_bp.route("", methods=["POST"])
# def handle_books():
#     request_body = request.get_json()
#     new_book = Book(title=request_body["title"],
#                     description=request_body["description"])

#     db.session.add(new_book)
#     db.session.commit()

#     return make_response(f"Book {new_book.title} successfully created", 201)

# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Fictional Book", "A fantasy novel set in an imaginary world."),
#     Book(2, "Wheel of Time", "A fantasy novel set in an imaginary world."),
#     Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
# ]
