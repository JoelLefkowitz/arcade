from aiohttp.web import get, post

from .views import ScoresView

urlpatterns = [get("/api/scores", ScoresView.get), post("/api/scores", ScoresView.post)]
