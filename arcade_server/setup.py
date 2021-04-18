from functools import reduce
from typing import Any, Dict, List, cast

from setuptools import setup

configuration = {
    "install_requires": [
        "django-debug-toolbar",
        "django-extensions",
        "django-silk",
        "django",
        "djangorestframework",
        "drf-yasg",
        "randutils",
        "gunicorn",
        "psycopg2",
        "safe_environ"
    ],
    "extras_require": {
        "tests": ["mock"],
        "linters": [
            "mypy",
            "pylint",
            "bandit",
        ],
        "formatters": [
            "autoflake",
            "black",
            "isort",
        ],
        "runtests": [
            "coverage",
            "codacy-coverage",
            "pytest-bdd",
            "pytest-cov",
            "pytest-html",
            "pytest-sugar",
            "pytest-watch",
            "pytest",
            "tox-travis",
            "tox",
        ],
        "docs": ["quickdocs"],
        "publishers": [
            "twine",
            "wheel",
            "bump2version",
        ],
    },
}

if __name__ == "__main__":
    extras_require = cast(
        Dict[Any, List[Any]], configuration["extras_require"]
    )

    merge_lists = lambda acc, x: list(set(acc) | (set(x)))

    configuration["extras_require"] = dict(
        **extras_require,
        **{"all": reduce(merge_lists, extras_require.values())}
    )

    setup(**configuration)
