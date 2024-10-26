
from psnawp_api import PSNAWP


class PSNAPIClient:
    psnawp_client: PSNAWP
    def __init__(self, sso_code: str) -> None:
        self.psnawp_client = PSNAWP(sso_code)
    
    def me(self):
        return self.psnawp_client.me()
    
    def get_account_devices(self):
        user = self.psnawp_client.me()
        return user.get_account_devices()
    
    def get_account_friends(self):
        user = self.psnawp_client.me()
        return user.friends_list()

    def get_account_blocked(self):
        user = self.psnawp_client.me()
        return user.blocked_list()
    
    def get_my_games(self):
        user = self.psnawp_client.me()
        games = user.title_stats()
        result = []
        for x in list(games):
            game_dict = {
                'id': x.title_id,
                'name': x.name,
                'imageUrl': x.image_url,
                'duration': {
                    'hours': x.play_duration.seconds // 3600,
                    'minutes': (x.play_duration.seconds % 3600) // 60
                }
            }
            result.append(game_dict)
        return result