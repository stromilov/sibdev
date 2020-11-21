#urls.py

from django.urls import path

from .views import APIDeals

from .form import upload_file


urlpatterns = [
    path('deals/', APIDeals.as_view()),
    path('form/', upload_file),
]