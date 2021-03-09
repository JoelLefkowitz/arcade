from inspect import cleandoc

from browser import window
from rest import post_score
from utils import ordinal


def show_results(score, top_scores):
    modal = window.jQuery("#resultsModal")
    modal.html(create_modal(score, top_scores))

    post_score_buttton = window.jQuery("#postScore")
    player_name = window.jQuery("#playerName")

    post_score_buttton.on(
        "click",
        lambda x: post_score(player_name.val() or "Name", score),
    )

    post_score_buttton.on("click", lambda x: modal.modal("toggle"))

    modal.modal("toggle")


def create_modal(score, top_scores):
    return cleandoc(
        f"""
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    {modal_header()}
                </div>
                <div class="modal-body">                                    
                    {results(score)}
                    <h5>Leaderboard</h5>
                    {leaderboard(top_scores)}
                </div>
                <div class="modal-footer">
                    {modal_footer()}
                </div>
            </div>
        </div>    
        """
    )


def modal_header():
    return cleandoc(
        f"""
        <h5 class="modal-title">Results</h5>
            <button
                type="button"
                class="close"
                data-dismiss="modal"
                aria-label="Close"
            >
            <span aria-hidden="true">&times;</span>
        </button>
        """
    )


def results(score):
    return cleandoc(
        f"""
        <div class="container">
            <div class="row">
                <div class="col">Your score:</div>
                <div class="col">{score}</div>
            </div>
            <div class="row">
                <div class="col full-lines">Your name:</div>
                <div class="col">
                <input
                    id="playerName"
                    type="text"
                    class="form-control form-field"
                    placeholder="Name"
                    aria-label="Name"
                    aria-describedby="basic-addon1"
                />
                </div>
            </div>
        </div>
        """
    )


def leaderboard(top_scores):
    return (
        '<div class="container">'
        + "\n".join(
            [
                cleandoc(
                    f"""
                    <div class="row">
                        <div class="col">{ordinal(i + 1)}:</div>
                        <div class="col">{score["name"]}</div>
                        <div class="col">{score["value"]}</div>
                    </div>
                    """
                )
                for i, score in enumerate(top_scores)
            ]
        )
        + "</div>"
    )


def modal_footer():
    return cleandoc(
        f"""
        <button type="button" class="btn btn-secondary" id="postScore">
            Post score
        </button>
        <button type="button" class="btn btn-secondary" data-dismiss="modal">
            Close
        </button>
        """
    )
