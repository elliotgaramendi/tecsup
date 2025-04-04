from django.shortcuts import render
from .models import Item


def item_list(request):
    items = Item.objects.all()
    return render(request, 'core/item_list.html', {'items': items})
