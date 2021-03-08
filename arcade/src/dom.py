from inspect import cleandoc

from browser import window


def show_results(score, top_scores):
    modal = window.jQuery("#resultsModal")
    modal.modal("show")
    modal.html(
        cleandoc(
            f"""
            <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                <h5 class="modal-title">Results</h5>
                <button
                    type="button"
                    class="close"
                    data-dismiss="modal"
                    aria-label="Close"
                >
                    <span aria-hidden="true">&times;</span>
                </button>
                </div>

                <div class="modal-body">
                    <div class="container">
                        <div class="row">
                            <div class="col">
                            Your score:
                            </div>
                            <div class="col">
                            {score}
                            </div>
                        </div>
                        <div class="row">
                            <div class="col full-lines">
                            Your name:
                            </div>
                            <div class="col">
                            <input type="text" class="form-control form-field" placeholder="Name" aria-label="Username" aria-describedby="basic-addon1">
                            </div>
                        </div>
                    </div>
                    
                    <h5>Leaderboard</h5>

                    <div class="container">
                        <div class="row">
                            <div class="col">
                            1st:
                            </div>
                            <div class="col">
                            Name
                            </div>
                            <div class="col">
                            Score
                            </div>
                        </div>
                    </div>
                </div>

                <div class="modal-footer">
                <button type="button" class="btn btn-secondary" id="postScore">
                    Post score
                </button>
                
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                </div>
            </div>
            </div>    
            """
        )
    )
