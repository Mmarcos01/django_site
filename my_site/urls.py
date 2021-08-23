from django.urls import path
from .views import HomeView, AboutView, PoetryView

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('poetry', PoetryView.as_view(), name='poetry'),
]
