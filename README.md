Brasil.com.vc
=============


Installation
------------

1. Setup a new virtualenv: `virtualenv .venv`
2. Install requirements: `pip install -r requirements.txt`
3. Run tests to check setup: `python manage.py test`
4. [Configure your environment](#environment-settings).


Environment settings
--------------------

Before running the Django server locally, you should set some environment-
specific values, as defined below:

- `BASE_URL` - Main URL where the app will be available
- `DATABASE_URL` - Database connection URL (eg. `postgres://user:pass@server:port/db`)
- `DEBUG` - Set debug mode (`'true'` or `'false'`)
- `SECRET_KEY` - Unique and secret salt for passwords, hashes and session keys
- `DEFAULT_FROM_EMAIL` - Email address to identify outcoming transactional emails


Setup static files
------------------

You must set up Node.js in order to make static files gathering and processing
work. We already include nodeenv to help with that:

- Install Node + npm: `nodeenv -p --prebuilt`
- Install required packages: `nodeenv --requirements=requirements.npm.txt --update $VIRTUAL_ENV`

