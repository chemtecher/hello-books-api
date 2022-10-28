
from flask import Blueprint, jsonify, abort, make_response

# books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

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


# #Read All books
# @books_bp.route("", methods=["GET"])
# def handle_books():
#     books_response = []
#     for book in books:
#         books_response.append(
#             {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }
#         )
#     return jsonify(books_response)


# # #Find One Book without Refactoring
# # @books_bp.route("/<book_id>", methods=["GET"]) #postman request => url + /books/3 where 3 == book_id
# # def handle_book(book_id):
# #     # Handling an invalid book_id
# #     try:
# #         book_id = int(book_id)
# #     except:
# #         return {"message":f"book {book_id} invalid"}, 400

# #     for book in books:
# #         if book.id == book_id:
# #             return {
# #                 "id": book.id,
# #                 "title": book.title,
# #                 "description": book.description,
# #             }
# #     # Handling a non-existing book
# #     return {"message":f"book {book_id} not found"}, 404 

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