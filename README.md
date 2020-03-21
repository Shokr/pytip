# Daily Python Tips

- Tweetify


### Install
* pip install virtualenv
* cd pytip
* virtualenv env
* source env/bin/activate
* pip install requirements.txt
* python manage.py runserver

=> Change Setting in config/settings/base.py
  
#### Admin Auth
- username  : shokr
- password  : 123456789
- api_token : 2bef4238ba0de2f69c09095b17316c7a174d057d

### Run Server 
- gunicorn config.wsgi

### Run celery tasks.
-  celery -A config beat -l info

#
### Accessibility
#####- Admin:
 http://127.0.0.1:8000/admin/

#####- Api: 
* curl http://127.0.0.1:8000/api/Tweets/ -H 'Authorization: Token 2bef4238ba0de2f69c09095b17316c7a174d057d'
* curl http://127.0.0.1:8000/api/Tweets/5/ -H 'Authorization: Token 2bef4238ba0de2f69c09095b17316c7a174d057d'

* curl http://127.0.0.1:8000/api/users/ -H 'Authorization: Token 2bef4238ba0de2f69c09095b17316c7a174d057d'