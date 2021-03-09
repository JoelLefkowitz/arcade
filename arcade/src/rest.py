import json
from urllib.error import HTTPError

from browser import ajax


def get_top_scores(callback=None):
    ajax.get(
        "api/scores", oncomplete=lambda x: oncomplete(x, callback)
    )


def post_score(name, score, callback=None):
    ajax.post(
        "api/scores",
        oncomplete=lambda x: oncomplete(x, callback),
        data={"name": name, "value": score},
    )


def oncomplete(x, callback):
    if x.status >= 400:
        raise HTTPError

    if callback:
        return callback(json.loads(x.text))
