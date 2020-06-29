import requests
from celery import Celery

BROKER_URL = "redis://redis:6379/0"
BACKEND_URL = "redis://redis:6379/1"
# CELERY_RESULT_EXPIRES = 86400

# Run Celery using Redis broker/backend
app = Celery("tasks", broker=BROKER_URL, backend=BACKEND_URL)


@app.task
def get_rates(base_currency, target_currency):
    """
    Get daily rates from api.ratesapi.io
    """
    url = "https://api.ratesapi.io/api/latest?base=%s&symbols=%s" % (
        base_currency,
        target_currency,
    )
    print("Requesting ", url)
    r = requests.get(url)
    root = r.json()
    print("Returned ", root)
    rates = root.get("rates")
    return rates.get(target_currency)


if __name__ == "__main__":
    app.start()
