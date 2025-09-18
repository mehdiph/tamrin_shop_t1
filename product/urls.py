from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.comment_form, name='comment_form')
]