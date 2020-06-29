from aiohttp import web
from tasks import get_rates

currencies = ["CZK", "EUR", "PLN", "USD"]


async def handle_conversion(request):
    """
    Handle currency conversion
    Example: localhost:8080/convert&from=EUR&to=CZK&amount=100
    """

    base_currency = request.match_info.get("from")
    if base_currency not in currencies:
        # raise ValueError('Currency %s not supported' % base_currency)
        return web.Response(text="Currency %s not supported" % base_currency)

    target_currency = request.match_info.get("to")
    if target_currency not in currencies:
        # raise ValueError('Currency %s not supported' % target_currency)
        return web.Response(text="Currency %s not supported" % target_currency)
    try:
        amount = float(request.match_info.get("amount"))
    except ValueError:
        # raise ValueError('Amount is not integer')
        return web.Response(text="Amount is not a number")

    result = get_rates.delay(base_currency, target_currency).get()
    converted_amount = amount * result

    return web.Response(text=str(converted_amount))


async def handle_stats(request):
    params = request.rel_url.query
    return web.Response(text=params)


app = web.Application()
# app.add_routes([web.get('/convert', handle_conversion),
#                web.get('/stats', handle_stats)])

app.add_routes(
    [
        web.get("/convert&from={from}&to={to}&amount={amount}", handle_conversion),
        web.get("/stats", handle_stats),
    ]
)

if __name__ == "__main__":
    # Runs at 0.0.0.0:8080
    web.run_app(app)
