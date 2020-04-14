from cryptocompsdk.social.current.parse import CouldNotGetSocialLatestException
from cryptocompsdk.request import APIBase
from cryptocompsdk.urls import SOCIAL_LATEST_URL


class SocialLatestAPI(APIBase):
    _exception_class = CouldNotGetSocialLatestException

    # TODO: add typing
    def get(self, coin_id: int = 1182):
        payload = dict(
            coinId=coin_id,
        )

        return self._get_one_or_paginated(SOCIAL_LATEST_URL, payload=payload)

    # TODO: add class factory and typing
    def _class_factory(self, data: dict):
        return data
