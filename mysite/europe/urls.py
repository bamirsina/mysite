from django.urls import path
from mysite.mysite import views

urlpatterns = [
    path("", views.index)
]
