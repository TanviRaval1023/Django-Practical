from django.urls import path
from . import views

urlpatterns = [
    path('', views.analyze_sentiment, name='analyze_sentiment'),
]