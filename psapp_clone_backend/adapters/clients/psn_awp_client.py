
from psnawp_api import PSNAWP


class PSNAPIClient:
    psnawp_client: PSNAWP
    def __init__(self, sso_code: str) -> None:
        self.psnawp_client = PSNAWP(sso_code)
    
    def me(self):
        return self.psnawp_client.me()