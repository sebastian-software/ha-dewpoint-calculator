# Development Guide

## Releasing a New Version

To publish a new release of the Dewpoint Calculator:

1. Merge all changes into the `main` branch
2. Update the version number in `custom_components/dewpoint_calculator/manifest.json`
3. Go to **Releases** → **Draft a new release**
4. Click **Choose a tag** → **Create new tag**
5. Create a tag using the format `v1.2.3`
6. Add a release title and description
7. Click **Publish release**

## Running sensor tests

Use Python 3.14 with the pinned Home Assistant test dependency:

```sh
python3.14 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-test.txt
python -m pytest tests/
```

The tests use synthetic source states and require no devices or running Home Assistant server.
