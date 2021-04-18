from aiohttp.web import get
from aiohttp.web import post

from .views import ScoresView

urlpatterns = [
    get("/api/scores", ScoresView.get),
    post("/api/scores", ScoresView.post),
]
