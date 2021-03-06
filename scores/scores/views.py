from aiohttp.web import View, json_response
from .db import select_rows
from .models import Score


class ScoresView(View):
    async def get(self):
        data = [i async for i in select_rows()]
        return json_response(data)

    async def post(self):
        # data = Score(name=self.request.name, score=self.request.score)
        data = {}
        response = json_response(data)
        await response.prepare(self.request)
        await response.write_eof()
