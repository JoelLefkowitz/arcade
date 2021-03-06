from setuptools import setup

if __name__ == "__main__":
    setup(
        entry_points={"console_scripts": ["quickdocs = quickdocs.__main__:main"]},
        install_requires=[
            "aiopg",
            "asyncio",
            "dataclasses",
            "gunicorn",
            "safe_environ",
        ],
        extras_require={
            "tests": [
                "pytest-bdd",
                "pytest-cov",
                "pytest-html",
                "pytest-sugar",
                "pytest-watch",
                "pytest",
                "tox-travis",
                "tox",
            ],
            "tools": [
                "autoflake",
                "bandit",
                "black",
                "bump2version",
                "isort",
                "mypy",
                "pylint",
                "quickdocs",
                "twine",
                "wheel",
            ],
        },
    )
