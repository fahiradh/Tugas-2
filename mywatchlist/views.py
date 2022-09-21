from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    data = WatchlistItem.objects.all()
    
    watched = 0
    total_movie = data.count()
    for mov in data:
        if (mov.watched == True):
            watched += 1
    if watched >= (total_movie-watched):
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"   
    
    context = {
        'data_film': data,
        'nama': 'Fahira Adindiah',
        'npm': '2106751575',
        'message': message,
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")