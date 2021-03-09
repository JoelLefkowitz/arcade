from aiohttp.web import HTTPUnprocessableEntity, View, json_response

from .db import get_top_scores, insert_score
from .models import Score


class ScoresView(View):
    async def get(self):
        leaders = await get_top_scores()
        return json_response([score.data for score in leaders])

    async def post(self):
        data = await self.post()

        if "name" not in data or "value" not in data:
            raise HTTPUnprocessableEntity

        score = Score(data["name"], data["value"])

        await insert_score(score)
        return json_response(score.data)
