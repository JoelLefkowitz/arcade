from browser import ajax


def get_top_scores(oncomplete=None):
    ajax.get("api/scores", oncomplete=oncomplete)


def post_score(name, score, oncomplete=None):
    ajax.post(
        "api/scores",
        oncomplete=oncomplete,
        data={"name": name, "value": score},
    )
