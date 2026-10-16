# GitHub workflows for Python and Django

The demo project for [GitHub Workflows for Python and Django (Step by Step)](https://my-space.io/blog/github-workflows/) on my-space.io.

Taskboard is a small Django 6.1 app that runs in Docker with PostgreSQL. The post adds GitHub workflows to it one step at a time, and the runs in this repo's Actions tab came from following those steps.

- The `start` branch is the app and its tests, with no workflows yet. Begin the tutorial there.
- The `main` branch has the finished workflows in `.github/workflows/`.

## The workflows

- `ci.yml` runs on every pull request, every push to `main` and by hand from the Actions tab. It tests on Python 3.12, 3.13 and 3.14 against PostgreSQL 18, then builds the Docker image and requests the status page from the running container.
- `release.yml` runs when you push a version tag such as `v0.1.0`. It calls `ci.yml` first, then publishes the image to GitHub Container Registry.
- `.github/dependabot.yml` opens a pull request when one of the actions has a new release.

The `main` branch has a ruleset, so nothing merges until all four CI checks pass.

## Run the tests on your machine

The status page reads the PostgreSQL version, so the tests need PostgreSQL, not SQLite.

```bash
docker run -d --name taskboard-pg -e POSTGRES_PASSWORD=dev-password -e POSTGRES_DB=app -p 5432:5432 postgres:18-alpine
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export SECRET_KEY=dev-only-key DATABASE_URL=postgresql://postgres:dev-password@localhost:5432/app
python manage.py collectstatic --noinput
python manage.py test
```

The Docker setup comes from [How to Run Django in Docker With PostgreSQL (Step by Step)](https://my-space.io/blog/django-docker/).
