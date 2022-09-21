from django.urls import path
from mywatchlist.views import show_watchlist, show_xml, show_json
#from mywatchlist.views import show_xml, show_json #sesuaikan dengan nama fungsi yang dibuat

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
    path('html/', show_watchlist, name='show_watchlist'),
    path('xml/', show_xml, name='show_xml'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/', show_json, name='show_json'), #sesuaikan dengan nama fungsi yang dibuat
]