from django.urls import path
from skyrim.presenters.selectcharacter.views import select_character_view

app_name = 'select_character'

urlpatterns = [
    path('<int:battle_id>/',select_character_view,name = 'list_player')
]