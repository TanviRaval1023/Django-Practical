from django.shortcuts import render, redirect, get_object_or_404
from .models import Book


# Display all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


# Add a new book
def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        author = request.POST.get('author', '').strip()
        price = request.POST.get('price', '').strip()
        genre = request.POST.get('genre', '').strip()
        published_year = request.POST.get('published_year', '').strip()

        if title and author and price and genre and published_year:
            try:
                price_value = float(price)
                year_value = int(published_year)

                if price_value < 0 or year_value < 0:
                    raise ValueError

                Book.objects.create(
                    title=title,
                    author=author,
                    price=price_value,
                    genre=genre,
                    published_year=year_value
                )

                return redirect('book_list')

            except (ValueError, OverflowError):
                return render(request, 'books/book_form.html', {
                    'error': 'Enter a valid price and publication year.',
                    'book': request.POST
                })

        return render(request, 'books/book_form.html', {
            'error': 'All fields are required.',
            'book': request.POST
        })

    return render(request, 'books/book_form.html')


# Update an existing book
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        author = request.POST.get('author', '').strip()
        price = request.POST.get('price', '').strip()
        genre = request.POST.get('genre', '').strip()
        published_year = request.POST.get('published_year', '').strip()

        if title and author and price and genre and published_year:
            try:
                price_value = float(price)
                year_value = int(published_year)

                if price_value < 0 or year_value < 0:
                    raise ValueError

                book.title = title
                book.author = author
                book.price = price_value
                book.genre = genre
                book.published_year = year_value
                book.save()

                return redirect('book_list')

            except (ValueError, OverflowError):
                return render(request, 'books/book_form.html', {
                    'error': 'Enter a valid price and publication year.',
                    'book': book,
                    'form_data': request.POST
                })

        return render(request, 'books/book_form.html', {
            'error': 'All fields are required.',
            'book': book,
            'form_data': request.POST
        })

    return render(request, 'books/book_form.html', {'book': book})


# Delete a book
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()

    return redirect('book_list')
