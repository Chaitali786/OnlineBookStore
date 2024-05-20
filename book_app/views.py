from django.shortcuts import render
from .models import Book, CartItem
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
 
 
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.urls import reverse
# Create your views here.

def index(request):
    return render (request , 'index.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookstore/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'bookstore/book_detail.html', {'book': book})

def user_login(request):
 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
 
        user = authenticate(username=username,password=password)
 
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('book_list'))
           
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE!")
           
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")
   
    else:
        return render(request, 'user_authentication/login.html',{})
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('book_list'))

#def user_logout(request):
    #logout(request)
    #return render(request, 'basic_app/logout.html')



# Implement search functionality in views.py

def search_results(request):
    query = request.GET.get('query')

    # Filter books based on search query
    books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)

    return render(request, 'bookstore/book_list.html', {'books': books, 'query': query})
#Add to cart book 
@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('book_list')  # Redirect to the book list page or another appropriate page

@login_required
def get_cart_items(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        # Serialize cart items to JSON
        data = [{'book': {'title': item.book.title}, 'quantity': item.quantity} for item in cart_items]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'User is not authenticated'}, status=401)