from aiohttp import web
from enum import Enum, unique

@unique
class Currency(Enum):
    CZK = 1
    EUR = 2
    PLN = 3
    USD = 4

async def handle_conversion(request):
    params = request.rel_url.query
    from_currency = params['from']
    
    if from_currency not in Currency.__members__.items():
        raise ValueError('Currency %s not supported' % from_currency)
        
    to_currency = params['to']
    if to_currency not in Currency.__members__.items():
        raise ValueError('Currency %s not supported' % to_currency)
        
    try:
        amount = params['amount']
    except ValueError:
        raise ValueError('Amount is not integer')
    
    converted_amount = None
    if from_currency == 'CZK' and to_currency == 'EUR':
        result = get_rates_czk_eur.apply_async()
    
    elif from_currency == 'CZK' and to_currency == 'PLN':
        result = get_rates_czk_pln.apply_async()
    
    elif from_currency == 'CZK' and to_currency == 'USD':
        result = get_rates_czk_usd.apply_async()
    
    elif from_currency == 'EUR' and to_currency == 'CZK':
        result = get_rates_eur_czk.apply_async()
        
    elif from_currency == 'EUR' and to_currency == 'PLN':
        result = get_rates_eur_pln.apply_async()
    
    elif from_currency == 'EUR' and to_currency == 'USD':
        result = get_rates_eur_usd.apply_async()
    
    elif from_currency == 'PLN' and to_currency == 'CZK':
        result = get_rates_pln_czk.apply_async()
    
    elif from_currency == 'PLN' and to_currency == 'EUR':
        result = get_rates_pln_eur.apply_async()
    
    elif from_currency == 'PLN' and to_currency == 'USD':
        result = get_rates_pln_usd.apply_async()

    elif from_currency == 'USD' and to_currency == 'CZK':
        result = get_rates_usd_czk.apply_async()

    elif from_currency == 'USD' and to_currency == 'EUR':
        result = get_rates_usd_eur.apply_async()

    elif from_currency == 'USD' and to_currency == 'PLN':
        result = get_rates_usd_pln.apply_async()
                
    converted_amount = amount * result.get()                                       
        
    return web.Response(text=converted_amount)

async def handle_stats(request):
    params = request.rel_url.query
    return web.Response(text=params)
    
# "convert" - convert one currency to another  
# https://api.currencylayer.com/convert?from=EUR&to=GBP&amount=100 
app = web.Application()
app.add_routes([web.get('/convert', handle_conversion),
                web.get('/stats', handle_stats)])

if __name__ == '__main__':
    # Runs at 0.0.0.0:8080
    web.run_app(app)
    