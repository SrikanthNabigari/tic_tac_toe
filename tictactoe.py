from google.appengine.ext import endpoints
from protorpc import remote

from protorpc import message_types
from protorpc import messages

from models import Profile
from models import ScoreBoard

CLIENT_ID = '161967083643-8eeiff4p5dr1mk31sq2geagciuev3sur.apps.googleusercontent.com'

@endpoints.api(name='tictactoe', version='v1',
               description='Tic Tac Toe API',
               allowed_client_ids=[CLIENT_ID, endpoints.API_EXPLORER_CLIENT_ID])
class TicTacToeApi(remote.Service):

    def get_profile_user(raise_unauthorized=True):
    """Return user Profile from datastore, creating new one if non-existent."""
        # make sure user is authed
        user = endpoints.get_current_user()
        if not user:
            raise endpoints.UnauthorizedException('Authorization required')

        # get Profile from datastore
        user_id = getUserId(user)
        p_key = ndb.Key(Profile, user_id)
        profile = p_key.get()
        # create new Profile if not there
        if not profile:
            profile = Profile(
                key = p_key,
                name = user.nickname(),
                email = user.email(),
            )
            profile.put()

        return profile

    @endpoints.method(message_types.VoidMessage, ScoreBoardResponse,
                      path='get-user-games', http_method='GET',
                      name='get_user_games')
    def get_user_games(self,request):
        usr = self.get_profile_user()
        


