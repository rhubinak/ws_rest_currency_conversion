from aiohttp import web
from main import handle_conversion


async def test_server(aiohttp_client, loop):
    app = web.Application()
    app.add_routes(
        [
            web.get("/convert&from={from}&to={to}&amount={amount}", handle_conversion),
            web.get("/stats", handle_stats),
        ]
    )
    client = await aiohttp_client(app)
    resp = await client.get("/convert")
    assert resp.status == 404
    resp = await client.get("/convert&from=DKK&to=EUR&amount=100")
    text = await resp.text()
    assert text == "Currency DKK not supported"

    resp = await client.get("/convert&from=EUR&to=DKK&amount=100")
    text = await resp.text()
    assert text == "Currency DKK not supported"

    resp = await client.get("/convert&from=CZK&to=EUR&amount=x")
    text = await resp.text()
    assert text == "Amount is not integer"
