#
#
#

import os, sys
import urllib.request
import http.client
import json

class AiApiError(Exception):
    pass

class AiApi:
    DEFAULT_URL = 'http://example.com/'
    DEFAULT_TIMEOUT = 30

    def __init__(self):
        env = os.environ
        self.api_url = env.get('AI_API_URL', AiApi.DEFAULT_URL)
        self.api_timeout = env.get('AI_API_TIMEOUT', AiApi.DEFAULT_TIMEOUT)

    def analysis(self, image_path: str):
        if not isinstance(image_path, str):
            raise AiApiError('image_path is not string')

        data = {'image_path': image_path}
        json_data = json.dumps(data).encode('utf-8')
        request = urllib.request.Request(
            self.api_url, method='POST', 
            headers={'Content-Type': 'application/json'},
            data=json_data)
        try:
            with urllib.request.urlopen(
                    request, timeout=self.api_timeout) as response:
                response_body = response.read().decode('utf-8')
                return json.loads(response_body.split('\n')[0])
        except urllib.error.HTTPError as exc:
            raise AiApiError('HTTP Error: ' + exc.reason) from exc

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass
