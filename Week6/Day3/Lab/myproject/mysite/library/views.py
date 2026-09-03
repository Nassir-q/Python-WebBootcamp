from django.shortcuts import render

# Create your views here.

books_db = [
    {"id": 1, "title": "Welcome to Django",
        "author": "Nasser Yassen", "year": 2026},
    {"id": 2, "title": "FastAPI demystifid",
        "author": "Abdullah Albassami", "year": 206}
]


def book_list(request):
    return render(request, 'library/book_list.html', {'books': books_db})


def book_detail(request, id):
    selected_book = None
    for book in books_db:
        if book['id'] == id:
            selected_book = book
            break

    return render(request, 'library/book_detail.html', {'book': selected_book})
