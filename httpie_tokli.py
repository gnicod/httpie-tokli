from httpie.plugins import AuthPlugin
from tokli.config import Config
from tokli.api import Api

__version__ = '0.1'
__author__ = 'Gaetan Nicod'
__licence__ = 'MIT Licence'


class TokliAuth:
    def __init__(self, name):
        self.name = name

    def __call__(self, r):
        api = Api(**Config.get_config_api(self.name))
        token = api.get_token()
        access_token = token['access_token']
        r.headers['Authorization'] = 'Bearer {}'.format(access_token)
        return r


class TokliPlugin(AuthPlugin):
    name = 'Tokli'
    auth_type = 'tokli'
    description = ''

    def get_auth(self, username, password):
        return TokliAuth(username)
