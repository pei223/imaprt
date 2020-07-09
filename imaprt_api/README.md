# imaprt API
- 画像処理GUIツールのバックエンド

## Setup
```
pip install -r requirements.txt
```


## 検証デプロイ
#### Developデプロイ(ブラウザ上で動作確認)
```
python manage.py runserver --settings=config.dev_settings
```

#### 通常デプロイ
```
python manage.py runserver --settings=config.prod_settings
```

## 本番デプロイ
```
gunicorn --env DJANGO_SETTINGSMODULE=config.prod_settings config.wsgi:application --bind <IP Address>:8000 -w 5 --threads 5 -D --log-syslog --access-logfile access.log --log-file error.log
```


## テスト
```
python manage.py test imaprt_api --settings=config.prod_settings
```

## テスト + カバレッジ算出
```
coverage run --source='./imaprt_api' manage.py test imaprt_api --settings=config.prod_settings
coverage report
coverage html
```