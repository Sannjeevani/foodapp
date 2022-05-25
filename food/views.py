from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite.forms import ItemForm
from .models import Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'Item_list'

def item(request):
    return HttpResponse('This is an item view.')    

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item'

@login_required
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form.html',{'form':form})

def update_item(request,item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance = item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form, 'item':item})

def delete_item(request,item_id):
    item = Item.objects.get(id=item_id)
    
    if request.method=='POST':
        item.delete()
        return redirect('food:index')

    return render(request,'food/item-delete.html',{'item':item})