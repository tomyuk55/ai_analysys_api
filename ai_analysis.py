##############################################################################
#
#
#

import time

class AiAnalysisError(Exception):
    pass

class AiAnalysis:

    def __init__(self, api, db):
        self.api = api
        self.db = db

    def process(self, image_path: str):
        if not isinstance(image_path, str):
            raise AiAnalysisError('image_path is not string')

        request_timestamp = int(time.time())
        result = self.api.analysis(image_path)
        response_timestamp = int(time.time())

        estimated_data = result.get('estimated_data', {})
        self.db.insert_analysis_log(
            image_path,
            result.get('success', ''),
            result.get('message', ''),
            estimated_data.get('class', 0),
            estimated_data.get('confidence', 0.0),
            request_timestamp, response_timestamp)

    def __call__(self, image_path: str):
        self.process(image_path)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

