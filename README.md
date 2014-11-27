Brasil.com.vc
=============

[![Build Status](https://travis-ci.org/brasilcomvc/brasilcomvc.svg)](https://travis-ci.org/brasilcomvc/brasilcomvc)


Installation
------------

1. Setup a new virtualenv: `virtualenv .venv`
2. Install requirements: `pip install -r requirements.txt`
3. Run tests to check setup: `python manage.py test`
4. [Configure your environment](#environment-settings).
5. [Setup static files](#setup-static-files)


Environment settings
--------------------

Before running the Django server locally, you should set some environment-
specific values, as defined below:

- `BASE_URL` - Main URL where the app will be available
- `DATABASE_URL` - Database connection URL (eg. `postgres://user:pass@server:port/db`)
- `DEBUG` - Set debug mode (`'true'` or `'false'`)
- `SECRET_KEY` - Unique and secret salt for passwords, hashes and session keys
- `DEFAULT_FROM_EMAIL` - Email address to identify outcoming transactional emails
- `EMAIL_HOST` - SMTP host name to be used for email sending
- `EMAIL_PORT` - SMTP port to be used for email sending
- `EMAIL_HOST_USER` - Username to authenticate on the SMTP server
- `EMAIL_HOST_PASSWORD` - Password to authenticate on the SMTP server


Setup static files
------------------

You must set up Node.js in order to make static files gathering and processing
work.

1. Install Node + npm. For OS X using Homebrew: `brew install npm`
2. Install required packages: `npm install`
   `npm` will call bower after install
