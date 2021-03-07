#!/usr/bin/env python

import os

from simple_pipes import pipe_call

default_version = "0.1.0_prod"

for (build_dir, build_name) in [
    ("arcade", "arcade"),
    ("scores", "scores"),
    ("db", "scores_db"),
]:
    pipe_call(
        [
            "docker",
            "build",
            os.path.normpath(
                os.path.join(__file__, "..", "..", build_dir)
            ),
            "-t",
            f"joellefkowitz/{build_name}:{default_version}",
        ]
    )
