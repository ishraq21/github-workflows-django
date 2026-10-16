#!/bin/sh
# Runs inside the container every time it starts.
set -e

echo "==> Running database migrations"
python manage.py migrate --noinput

echo "==> Collecting static files"
python manage.py collectstatic --noinput --clear

# Run the container's command: Gunicorn by default, or a one-off command.
exec "$@"
