from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.load_news,name='news'),
    path('news',views.load_news,name='news'),
]
    