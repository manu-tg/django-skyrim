from django.test import TestCase, RequestFactory
from skyrim.data.models import *
from skyrim.presenters.player.views import PlayerByUserView
from tests.presenters.abstract import ViewTest
from skyrim.presenters.views import create_player_view
               
class ListPlayerTest():
    def setUp(self):
        # need a browser customer 
        self.factory = RequestFactory()
        self.user = User.objects.create(username ='fred',email ='secret',
                                        password='top_secret')        

class CreatePlayerTest(ViewTest,TestCase):
    print("----------------CreatePlayerTest -----------------")
    
    function = create_player_view
    url = '/create_player/'
    template = 'create_player.html'

    def setUp(self):
        # TODO: Populate para poder testear  get_all_player_races() y get_all_spells()
        return super().setUp()
    
    def get_response(self):
        response = self.client.get(self.url)
        return response
    
    
