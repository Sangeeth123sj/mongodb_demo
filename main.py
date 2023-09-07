import asyncio
import os
from database import db  # Import the 'db' object from your database.py file
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file if not already loaded

# Define a function to insert a new book into the database
async def insert_book(title, author, price):
    # Define the book document
    book = {
        "title": title,
        "author": author,
        "price": price
    }
    
    # Insert the book document into the "books" collection in the "demo_db"
    result = await db.books.insert_one(book)
    print(f"Inserted new book with ID: {result.inserted_id}")

# Define a function to list books from the database
async def list_books():
    # List book documents
    books_cursor = db.books.find({})  # Find all documents in the "books" collection

    # Create a list to store book titles
    book_list = []

    async for book in books_cursor:
        book_list.append(book.get('title'))
    print(book_list)

# Entry point of your application
async def main():
    # Get book details from user or any other source
    title = "Narnia Book"
    author = "CS Lewis"
    price = 19.99

    # Insert the book into the db
    await insert_book(title, author, price)

    # List all books added to db
    await list_books()

if __name__ == "__main__":
    asyncio.run(main())