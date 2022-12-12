from django.shortcuts import render
from .models import *

def index(request): 
    return render(request, 'pizzas/index.html')

def menu(request):
    menu = Pizza.objects.all()

    context = {'all_menu':menu}
    
    return render(request, 'pizzas/menu.html', context)

def item(request, item_id):
    pizza = Pizza.objects.get(id = item_id)
    
    entries = Comments.objects.filter( item = pizza)

    context = {'item':pizza, 'entries':entries}
    
    return render(request, 'pizzas/item.html', context)
    