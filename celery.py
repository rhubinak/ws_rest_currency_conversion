import settings
from celery import Celery

app = Celery('celery', include=['tasks'])

if __name__ == '__main__':
    app.start()
    