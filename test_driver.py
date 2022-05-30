#!/usr/bin/env python3

import os
from ai_api import AiApi
from ai_database import AiDatabase
from ai_analysis import AiAnalysis

if __name__ == '__main__':

    os.environ['AI_API_URL'] = 'http://localhost:8080/'

    with AiApi() as api:
        with AiDatabase() as db:
            with AiAnalysis(api, db) as analysis:
                analysis('/home/user/sample1.jpg')
                analysis('/home/user/sample2.jpg')
                analysis('/home/user/sample3.jpg')


