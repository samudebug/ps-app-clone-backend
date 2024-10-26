
from psnawp_api import PSNAWP
import psnawp_api


class PSNAPIClient:
    psnawp_client: PSNAWP
    def __init__(self, sso_code: str) -> None:
        self.psnawp_client = PSNAWP(sso_code)
    
    def me(self):
        return self.psnawp_client.me()
    
    def get_account_devices(self):
        user = self.me()
        return user.get_account_devices()
    
    def get_account_friends(self):
        user = self.me()
        return user.friends_list()

    def get_account_blocked(self):
        user = self.me()
        return user.blocked_list()
    
    def get_my_games(self):
        user = self.me()
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
    
    def get_trophy_groups(self, title_id: str):
        user = self.me()
        trophies = user.trophy_titles_for_title([title_id])
        communicationId = trophies.get_np_communication_id(trophies.authenticator, title_id, user.account_id)
        groups = user.trophy_groups_summary(np_communication_id=communicationId, platform=next(trophies).title_platform, include_progress=True)
        result = []
        for x in groups.trophy_groups:
            result.append({
                'id': x.trophy_group_id,
                'name': x.trophy_group_name,
                'detail': x.trophy_group_detail,
                'iconUrl': x.trophy_group_icon_url,
                'trophyCountInfo': {
                    'bronze': {
                        'total': x.defined_trophies.bronze,
                        'earned': x.earned_trophies.bronze
                    },
                    'silver': {
                        'total': x.defined_trophies.silver,
                        'earned': x.earned_trophies.silver,
                    },
                    'gold': {
                        'total': x.defined_trophies.gold,
                        'earned': x.earned_trophies.gold
                    },
                    'platinum': {
                        'total': x.defined_trophies.platinum,
                        'earned': x.earned_trophies.platinum
                    },
                }
            })
        return result
    

    def get_trophies_by_group(self, title_id: str, group_id: str):
        user = self.me()
        trophy_helper = user.trophy_titles_for_title([title_id])
        communicationId = trophy_helper.get_np_communication_id(trophy_helper.authenticator, title_id, user.account_id)
        trophies = user.trophies(np_communication_id=communicationId, platform=next(trophy_helper).title_platform, trophy_group_id=group_id, include_progress=True)
        result = []
        for x in trophies:
            result.append({
                'id': str(x.trophy_id),
                'type': x.trophy_type,
                'name': x.trophy_name,
                'detail': x.trophy_detail,
                'iconUrl': x.trophy_icon_url,
                'earned': x.earned
            })
        return result    

        