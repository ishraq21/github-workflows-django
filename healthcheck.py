"""Docker runs this to check the app. Exit code 0 means healthy."""
import os
import sys
import urllib.error
import urllib.request

# Django answers 400 when the Host header is not in ALLOWED_HOSTS,
# so send the first allowed host.
host = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')[0].strip()

request = urllib.request.Request(
    'http://localhost:8000/healthz',
    headers={'Host': host},
)

try:
    with urllib.request.urlopen(request, timeout=5) as response:
        sys.exit(0 if response.status == 200 else 1)
except (urllib.error.URLError, OSError):
    sys.exit(1)
