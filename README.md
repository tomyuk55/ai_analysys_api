# ai_analysys_api

## 内容物

- 実装
  - ai_analysis.py -- API呼び出しとそれに続くデータベース書き込み処理をカプセル化した実装
  - ai_api.py -- API呼び出しをカプセル化した実装
  - ai_database.py -- データベース処理をカプセル化した実装
- サプル&テスト
  - test_driver.py -- スタブWEBサーバーを利用して、実装をテストするサンプル
  - stub_server.py -- APIリクエストに対して、ダミーデータを返すスタブAPIサーバー
- その他
  - database_setup.sql -- データベース初期化SQL
