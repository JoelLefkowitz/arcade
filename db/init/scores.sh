#!/bin/sh
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE scores;
    CREATE TABLE scores_scores (
    Name varchar(255),
    Value int
);
EOSQL
