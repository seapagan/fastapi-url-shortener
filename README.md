# FastAPI-based URL Shortener

This is based on an original tutorial from [Real
Python](https://realpython.com/courses/url-shortener-fastapi/) which I
definitely recommend checking out for a decent example of a non-trivial
[FastAPI](https://fastapi.tiangolo.com/) app.

## Added Features

- `/list` (GET) route to return a list of all the URL's in the database along
  with their target.
- `/{url_key}/peek` (GET) route to show the target url of the specified urk=l_key,
  without actually redirecting there. Allows users or front-end client to check
  the URL before visiting.
- `/admin/{secret_key}` (PATCH) route to change the target URL of a link
  identified by the secret_key. The body of the request needs to have the
  `target_url` property containing the new URL which must be a valid URL
- The Root Path ("/") will return a short HTML template if viewed in a Web
  Browser, JSON otherwise.

## Planned Features

Non-exhaustive list of planned additions, in no specific order.

- Option to add a delay to the redirect, showing the exact target URL and giving
  the option to Cancel.
- User-friendly Front-end (probably in React) for adding and editing URLs.
- Protected ability to purge all `is_active: false` URLs
- Migrate away from SQLite, probably to a NO_SQL database with asyncio baked in.

## Development

Install the required dependency packages :

```bash
pip install -r requirements.txt
```

Run a local development server from the project root using `Uvicorn` :

```bash
uvicorn shortener_app.main:app --reload
```

Access the API at <http://localhost:8000>

See the API Docs at <http://localhost:8000/docs> or
<http://localhost:8000/redoc> for a list of the active endpoints
