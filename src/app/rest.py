import json
from browser import ajax


def get_top_scores(callback):
    ajax.get("api/scores", oncomplete=lambda x: oncomplete(x, callback))


def post_score(name, score, callback):
    ajax.post(
        "api/scores",
        oncomplete=lambda x: oncomplete(x, callback),
        data={"name": name, "value": score},
    )


def oncomplete(x, callback):
    return callback(json.loads(x.text)) if x.text else None
