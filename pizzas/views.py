from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request): 
    return render(request, 'pizzas/index.html')

def menu(request):
    menu = Pizza.objects.all()

    context = {'all_menu':menu}
    
    return render(request, 'pizzas/menu.html', context)

def pizzas(request, item_id):
    pizza = Pizza.objects.get(id = item_id)
    
    entries = Comments.objects.filter(item = pizza)

    context = {'item':pizza, 'entries':entries}
    
    return render(request, 'pizzas/item.html', context)

def comments(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data = request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.pizza = pizza
            comment.save()

            return redirect('MainApp:pizza', pizza_id = pizza_id)

        context = {'form':form, 'pizza':pizza}
        return render(request, 'MainApp/comment.html', context)