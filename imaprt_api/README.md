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
gunicorn --env DJANGO_SETTINGSMODULE=config.prod_settings config.wsgi:application --bind localhost:8000 -w 5 --threads 5
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