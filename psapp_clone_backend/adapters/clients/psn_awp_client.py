from typing import List
from psnawp_api import PSNAWP

from psapp_clone_backend.domain.interfaces.psn_api_client import IPSNAPIClient


class PSNAPIClient(IPSNAPIClient):
    psnawp_client: PSNAWP

    def __init__(self, sso_code: str, accept_language: str = "en-US") -> None:
        self.psnawp_client = PSNAWP(sso_code, headers={"Accept-Language": accept_language})

    def me(self):
        return self.psnawp_client.me()

    def get_my_profile(self):
        user = self.me()
        profile_dict = user.get_profile_legacy()["profile"]
        return {
            "id": profile_dict["accountId"],
            "username": profile_dict["onlineId"],
            "full_name": f"{profile_dict['personalDetail']['firstName']} {profile_dict['personalDetail']['lastName']}",
            "np_id": profile_dict["npId"],
            "avatar_urls": profile_dict["avatarUrls"],
            "about_me": profile_dict["aboutMe"],
        }

    def get_account_devices(self):
        user = self.me()
        devices = user.get_account_devices()
        result = []
        for x in [y for y in devices if y["activationType"] != "PSN"]:
            result.append(
                {
                    "device_id": x["deviceId"],
                    "device_type": x["deviceType"],
                    "activation_date": x["activationDate"],
                }
            )

        return result

    def get_account_friends(self):
        user = self.me()
        friends = user.friends_list()
        result = []
        for x in friends:
            presence = x.get_presence()
            profile_dict = x.profile()
            profile_dict["id"] = x.account_id
            profile_dict["presence"] = presence["basicPresence"]["primaryPlatformInfo"][
                "onlineStatus"
            ]
            result.append(profile_dict)
        return result

    def get_account_blocked(self):
        user = self.me()
        blocked = user.blocked_list()
        result = []
        for x in blocked:
            profile_dict = x.profile()
            profile_dict["id"] = x.account_id
            result.append(profile_dict)
        return result

    def get_my_games(self):
        user = self.me()
        games = user.title_stats()
        result = []
        for x in list(games):
            print(x)
            game_dict = {
                "id": x.title_id,
                "name": x.name,
                "imageUrl": x.image_url,
                "duration": {
                    "hours": x.play_duration.total_seconds() // 3600,
                    "minutes": (x.play_duration.total_seconds() % 3600) // 60,
                },
            }
            result.append(game_dict)
        return result

    def get_trophy_groups(self, title_id: str):
        user = self.me()
        trophies = user.trophy_titles_for_title([title_id])
        communicationId = trophies.get_np_communication_id(
            trophies.authenticator, title_id, user.account_id
        )
        groups = user.trophy_groups_summary(
            np_communication_id=communicationId,
            platform=next(trophies).title_platform,
            include_progress=True,
        )
        result = []
        for x in groups.trophy_groups:
            result.append(
                {
                    "id": x.trophy_group_id,
                    "name": x.trophy_group_name,
                    "detail": x.trophy_group_detail,
                    "iconUrl": x.trophy_group_icon_url,
                    
                    "trophyCountInfo": {
                        "bronze": {
                            "total": x.defined_trophies.bronze,
                            "earned": x.earned_trophies.bronze,
                        },
                        "silver": {
                            "total": x.defined_trophies.silver,
                            "earned": x.earned_trophies.silver,
                        },
                        "gold": {
                            "total": x.defined_trophies.gold,
                            "earned": x.earned_trophies.gold,
                        },
                        "platinum": {
                            "total": x.defined_trophies.platinum,
                            "earned": x.earned_trophies.platinum,
                        },
                    },
                }
            )
        return result

    def get_trophies_by_group(self, title_id: str, group_id: str):
        user = self.me()
        trophy_helper = user.trophy_titles_for_title([title_id])
        communicationId = trophy_helper.get_np_communication_id(
            trophy_helper.authenticator, title_id, user.account_id
        )
        trophies = user.trophies(
            np_communication_id=communicationId,
            platform=next(trophy_helper).title_platform,
            trophy_group_id=group_id,
            include_progress=True,
        )
        result = []
        for x in trophies:
            result.append(
                {
                    "id": str(x.trophy_id),
                    "type": x.trophy_type,
                    "name": x.trophy_name,
                    "detail": x.trophy_detail,
                    "iconUrl": x.trophy_icon_url,
                    "earned": x.earned,
                    "hidden": x.trophy_hidden,
                    "earnedDate": x.earned_date_time,
                }
            )
        return result

    def get_chats(self):
        user = self.me()
        chats = user.get_groups()
        result = []
        for x in chats:
            info = x.get_group_information()
            result.append(
                {
                    "id": info["groupId"],
                    "members": ", ".join(
                        [
                            y["onlineId"]
                            for y in info["members"]
                            if y["onlineId"] != user.online_id
                        ]
                    ),
                    "type": info["groupType"],
                    "name": info["groupName"]["value"],
                }
            )
        return result

    def get_conversation_for_chat(self, chat_id: str, limit: int = 20):
        chat = self.psnawp_client.group(group_id=chat_id)
        conversation = chat.get_conversation(limit=limit)
        result = []
        for message in conversation["messages"]:
            result.append(
                {
                    "id": message["messageUid"],
                    "body": message["body"],
                    "messageType": message["messageType"],
                    "createdAt": message["createdTimestamp"],
                    "sender": message["sender"]["onlineId"],
                }
            )
        return result

    def change_conversation_name(self, chat_id: str, name: str):
        chat = self.psnawp_client.group(group_id=chat_id)
        if chat.get_group_information()["groupType"] == 0:
            raise Exception("Cannot change name of a DM")
        chat.change_name(name)

    def send_message(self, chat_id: str, message: str):
        chat = self.psnawp_client.group(group_id=chat_id)
        chat.send_message(message)

    def create_group_chat(self, user_ids: List[str]):
        user = self.me()
        users = []
        for x in user_ids:
            users.append(self.psnawp_client.user(online_id=x))
        new_group = self.psnawp_client.group(users_list=users)
        info = new_group.get_group_information()
        return {
            "id": info["groupId"],
            "members": ", ".join(
                [
                    y["onlineId"]
                    for y in info["members"]
                    if y["onlineId"] != user.online_id
                ]
            ),
            "type": info["groupType"],
            "name": info["groupName"]["value"],
        }

    def leave_group_chat(self, chat_id: str):
        chat = self.psnawp_client.group(group_id=chat_id)
        chat.leave_group()

    def get_trophy_summary(self):
        user = self.me()
        summary = user.trophy_summary()
        print(summary)
        return {
            "total": summary.earned_trophies.bronze
            + summary.earned_trophies.silver
            + summary.earned_trophies.gold
            + summary.earned_trophies.platinum,
            "bronze": summary.earned_trophies.bronze,
            "silver": summary.earned_trophies.silver,
            "gold": summary.earned_trophies.gold,
            "platinum": summary.earned_trophies.platinum,
        }
