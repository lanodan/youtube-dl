# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class VocarooIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www.)?(voca.ro|vocaroo.com)/(?P<id>)'

    def _real_extract(self, url):
        hash_id = self._match_id(url)

        return {
            'id': hash_id,
            'url': 'https://media.vocaroo.com/mp3/' + hash_id
        }
