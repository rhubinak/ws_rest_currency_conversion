import requests
from .celery import app

@app.task
def get_rates_czk_eur():
    url = 'https://api.ratesapi.io/api/latest?base=CZK&symbols=EUR'
    r = requests.get(url)
    root = r.json()
    rates = root.rates
    return rates.EUR

@app.task
def get_rates_czk_pln():
    url = 'https://api.ratesapi.io/api/latest?base=CZK&symbols=PLN'
    r = requests.get(url)
    root = r.json()
    rates = root.rates
    return rates.PLN

@app.task
def get_rates_czk_usd():
    url = 'https://api.ratesapi.io/api/latest?base=CZK&symbols=USD'
    r = requests.get(url)
    root = r.json()
    rates = root.rates
    return rates.USD

@app.task
def get_rates_eur_czk():
    url = 'https://api.ratesapi.io/api/latest?base=EUR&symbols=CZK'
    r = requests.get(url)
    root = r.json()
    rates = root.rates
    return rates.CZK

@app.task
def get_rates_eur_pln():
    url = 'https://api.ratesapi.io/api/latest?base=EUR&symbols=PLN'
    r = requests.get(url)
    root = r.json()
    rates = root.rates
    return rates.PLN

@app.task
def get_rates_eur_usd():
    url = 'https://api.ratesapi.io/api/latest?base=EUR&symbols=USD'
    r = requests.get(url)
    root = r.json()
    rates = root.rates
    return rates.USD

@app.task
def get_rates_pln_czk():
    url = 'https://api.ratesapi.io/api/latest?base=PLN&symbols=CZK'
    r = requests.get(url)
    root = r.json()
    rates = root.rates
    return rates.CZK

@app.task
def get_rates_pln_eur():
    url = 'https://api.ratesapi.io/api/latest?base=PLN&symbols=EUR'
    r = requests.get(url)
    root = r.json()
    rates = root.rates
    return rates.EUR

@app.task
def get_rates_pln_usd():
    url = 'https://api.ratesapi.io/api/latest?base=PLN&symbols=USD'
    r = requests.get(url)
    root = r.json()
    rates = root.rates
    return rates.USD

@app.task
def get_rates_usd_czk():
    url = 'https://api.ratesapi.io/api/latest?base=USD&symbols=CZK'
    r = requests.get(url)
    root = r.json()
    rates = root.rates
    return rates.CZK

@app.task
def get_rates_usd_eur():
    url = 'https://api.ratesapi.io/api/latest?base=USD&symbols=EUR'
    r = requests.get(url)
    root = r.json()
    rates = root.rates
    return rates.EUR

@app.task
def get_rates_usd_pln():
    url = 'https://api.ratesapi.io/api/latest?base=USD&symbols=PLN'
    r = requests.get(url)
    root = r.json()
    rates = root.rates
    return rates.PLN
