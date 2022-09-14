from django.shortcuts import render
from katalog.models import CatalogItem


def show_katalog(request):
    data_item = CatalogItem.objects.all()
    context = {
        'data_item': data_item,
        'nama': 'Fahira Adindiah',
        'npm': '2106751575'
    }
    return render(request, "katalog.html", context)