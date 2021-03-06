#!/bin/sh
gunicorn my_app_module:my_web_app --bind localhost:8000 --worker-class aiohttp.GunicornWebWorker
