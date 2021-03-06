from aiohttp.web import Application, run_app
from .urls import urlpatterns

if __name__ == "__main__":
    app = Application()
    app.add_routes(urlpatterns)
    run_app(app)
