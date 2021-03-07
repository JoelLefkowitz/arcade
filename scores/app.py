from aiohttp.web import Application

from scores.urls import urlpatterns


async def app():
    app = Application()
    app.add_routes(urlpatterns)
    return app
