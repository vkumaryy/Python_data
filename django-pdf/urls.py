from django.urls import path
from .views import extract_text_and_show_in_notepad

urlpatterns = [
    path('extract-text/', extract_text_and_show_in_notepad, name='extract-text'),
]
