#!/bin/sh

set -e

gunicorn app:app                             \
    --bind 0.0.0.0:8080                      \
    --worker-class aiohttp.GunicornWebWorker 
