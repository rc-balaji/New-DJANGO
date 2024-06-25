from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem

def home(request):
    items = TodoItem.objects.all()
    return render(request, 'todolist_app/home.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        TodoItem.objects.create(title=title, description=description)
        return redirect('home')
    return render(request, 'todolist_app/add_item.html')

def edit_item(request, item_id):
    item = get_object_or_404(TodoItem, item_id=item_id)
    if request.method == 'POST':
        item.title = request.POST['title']
        item.description = request.POST.get('description', '')
        item.completed = 'completed' in request.POST
        item.save()
        return redirect('home')
    return render(request, 'todolist_app/edit_item.html', {'item': item})

def delete_item(request, item_id):
    item = get_object_or_404(TodoItem, item_id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request, 'todolist_app/delete_item.html', {'item': item})
