from browser import document, ajax

def get_top_scores(cb=None):
    ajax.get("api/scores", cb)


def post_score(name, score, cb=None):
    
    # headers={"Content-Type": "application/json"},
    ajax.post("api/scores", data={'name': name, 'score': score}, cb)
