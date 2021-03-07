FROM python:3.8.6

WORKDIR /scores

COPY setup.py setup.py
RUN pip install --upgrade pip
RUN pip install --no-cache-dir .

COPY . .
EXPOSE 8080/tcp
ENTRYPOINT ["/scores/entrypoint.sh"]
