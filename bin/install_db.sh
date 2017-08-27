#!/bin/bash

# determine os
if [ -z "$DATABASE_NAME" ]; then
    echo "Source ./env/database.sh"
    source ./env/database.sh
fi

# unameOut="$(uname -s)"
# case "${unameOut}" in
#     Darwin*)    pg_cmd="psql -U postgres";;
#     *)          pg_cmd="sudo -u postgres psql -h ${DATABASE_HOST}"
# esac

pg_cmd="psql -U postgres -h ${DATABASE_HOST} -w postgres"


${pg_cmd} -c "DROP DATABASE IF EXISTS ${DATABASE_NAME}"
${pg_cmd} -c "DROP ROLE IF EXISTS ${DATABASE_USERNAME}"
${pg_cmd} -c "CREATE USER ${DATABASE_USERNAME} WITH PASSWORD '${DATABASE_PASSWORD}';"
${pg_cmd} -c "CREATE DATABASE ${DATABASE_NAME} ENCODING 'UTF8';"
${pg_cmd} -c "GRANT ALL PRIVILEGES ON DATABASE ${DATABASE_NAME} TO ${DATABASE_USERNAME};"