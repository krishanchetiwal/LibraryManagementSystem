from django.shortcuts import render
from .models import Books

def home(request):
    books = Books.objects.all()
    return render(request, 'library/home.html', {'books': books})
def data(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('genre')and request.POST.get('author')and request.POST.get('section')and request.POST.get('shelf_no'):
            book = Books()
            book.name = request.POST.get('name')
            book.genre = request.POST.get('genre')
            book.author = request.POST.get('author')
            book.section = request.POST.get('section')
            book.shelf_no = request.POST.get('shelf_no')
            book.save()

            return render(request, 'library/data.html')

    else:
        return render(request, 'library/data.html')



