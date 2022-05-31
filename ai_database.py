#
# データベースアクセスをカプセル化して実装したクラス
#

import os
import MySQLdb

class AiDatabaseError(Exception):
    pass

class AiDatabase:
    DEFAULT_HOST = 'localhost'
    DEFAULT_USER = 'test'
    DEFAULT_PASSWORD = 'test'
    DEFAULT_DB_NAME = 'ai'

    def __init__(self):
        env = os.environ
        db_host = env.get('AI_DATABASE_HOST', AiDatabase.DEFAULT_HOST)
        db_user = env.get('AI_DATABASE_USER', AiDatabase.DEFAULT_USER)
        db_password = env.get('AI_DATABASE_PASSWORD', AiDatabase.DEFAULT_PASSWORD)
        db_name = env.get('AI_DATABASE_DB_NAME', AiDatabase.DEFAULT_DB_NAME)

        try:
            self.conn = MySQLdb.connect(
                host=db_host,
                user=db_user,
                passwd=db_password,
                db=db_name)
        except MySQLdb.Error as exc:
            raise AiDatabaseError(str(exc)) from exc

    def close(self):
        self.conn.close()

    def insert_analysis_log(self, image_path,
                            success, message, _class, confidence, 
                            request_timestamp, response_timestamp):

        sql = """
        INSERT INTO `ai_analysis_log` (
        `image_path`, `success`, `message`, `class`, `confidence`,
        `request_timestamp`, `response_timestamp`
        ) VALUES (
        %s, %s, %s, %s, %s, %s, %s
        )
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                sql,
                (image_path, success, message, _class, confidence,
                 request_timestamp, response_timestamp))
            self.conn.commit()
            cursor.close()
        except MySQLdb.Error as exc:
            raise AiDatabaseError(str(exc)) from exc
                           
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
