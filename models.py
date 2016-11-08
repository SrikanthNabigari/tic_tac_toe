from google.appengine.ext import endpoints
from google.appengine.ext import ndb

from protorpc import messages

class Profile(ndb.model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    wins = ndb.StringProperty(default = 0)
    loses = ndb.StringProperty(default = 0)
    draw = ndb.SringProperty(default = 0)


class ScoreBoard(ndb.model):
    outcome = ndb.StringProperty(required=True)
    played = ndb.DateTimeProperty(auto_now_add=True)
    player = ndb.StructuredProperty(Profile)

class ProfileResponse(messages.Message):
    name = messages.StringField(1)
    email = messages.StringField(2)
    wins = messages.StringField(3)
    loses = messages.StringField(4)
    draw = messages.StringField(5)    

class ScoreBoardResponse(messages.Message):
    outcome = messages.StringField(1)
    played = messages.StringField(2)
    player = messages.StringField(3)