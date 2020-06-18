cd ./imaprt_api
start /min python manage.py runserver --settings=config.prod_settings >> api_log.log
cd ../imaprt_frontend
start /min npm run start >> front_log.log
cd ..