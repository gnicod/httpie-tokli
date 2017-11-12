from httpie.plugins import AuthPlugin
from tokli.config import Config
from tokli.api import Api

__version__ = '0.1'
__author__ = 'Gaetan Nicod'
__licence__ = 'MIT Licence'


class TokliAuth:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def __call__(self, r):
        force_refresh = self.action == 'refresh'
        api = Api(**Config.get_config_api(self.name),
                  force_refresh=force_refresh)
        token = api.get_token()
        access_token = token['access_token']
        r.headers['Authorization'] = 'Bearer {}'.format(access_token)
        return r


class TokliPlugin(AuthPlugin):
    name = 'Tokli'
    auth_type = 'tokli'
    description = ''

    def get_auth(self, username, password):
        return TokliAuth(username, password)
