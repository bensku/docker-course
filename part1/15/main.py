from aiohttp import web

async def say_hello(request):
    return web.Response(text='Hello from Docker!')

async def status(request):
    return web.Response(text='OK')

app = web.Application()
app.add_routes([web.get('/hello', say_hello),
                web.get('/status', status)])

if __name__ == '__main__':
    web.run_app(app)