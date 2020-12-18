from django.shortcuts import render, redirect
from shop.models import Movie
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

@login_required()
def cart_add(request, id):
    cart = Cart(request)
    product = Movie.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required()
def cart_detail(request):
    return render(request, 'cart_detail.html')