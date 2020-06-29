from aiohttp import web
from enum import Enum, unique
from tasks import get_rates_czk_eur

@unique
class Currency(Enum):
    CZK = 1
    EUR = 2
    PLN = 3
    USD = 4

async def handle_conversion(request):
    params = request.rel_url.query
    base_currency = params['from']
    
    if base_currency not in Currency.__members__.items():
        raise ValueError('Currency %s not supported' % base_currency)
        
    target_currency = params['to']
    if target_currency not in Currency.__members__.items():
        raise ValueError('Currency %s not supported' % target_currency)
        
    try:
        amount = params['amount']
    except ValueError:
        raise ValueError('Amount is not integer')
    
    result = get_rates_czk_eur.apply_async(base_currency, target_currency)
    #result = get_rates_czk_eur.delay(base_currency, target_currency)
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
    