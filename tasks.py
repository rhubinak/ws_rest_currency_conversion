import requests
import settings
from celery import Celery

app = Celery('tasks')

@app.task
def get_rates(base_currency, target_currency):
    url = 'https://api.ratesapi.io/api/latest?base=%s&symbols=%s' % (base_currency, target_currency)
    r = requests.get(url)
    root = r.json()
    rates = root.rates
    return rates[target_currency]
    
if __name__ == '__main__':
    app.start()
    