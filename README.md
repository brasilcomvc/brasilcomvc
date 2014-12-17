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

- `BASE_URL` - Main URL where the app will be available (NO TRAILING SLASH!)
- `DATABASE_URL` - Database connection URL (eg. `postgres://user:pass@server:port/db`)
- `DEBUG` - Set debug mode (`'true'` or `'false'`)
- `DEFAULT_FROM_EMAIL` - Email address to identify outcoming transactional emails
- `EMAIL_HOST_PASSWORD` - Password to authenticate on the SMTP server
- `EMAIL_HOST_USER` - Username to authenticate on the SMTP server
- `EMAIL_HOST` - SMTP host name to be used for email sending
- `EMAIL_PORT` - SMTP port to be used for email sending
- `FACEBOOK_APP_KEY` - Facebook app key (used for registration)
- `FACEBOOK_APP_SECRET` - Facebook app secret (used for registration)
- `MAILING_ADDRESS` - Physical address of the organization running the project
- `SECRET_KEY` - Unique and secret salt for passwords, hashes and session keys
- `SENTRY_DSN` - Optional. Use this to configure your Sentry DSN.
- `SNS_FACEBOOK` - URL of the Facebook fan page
- `SNS_GOOGLEPLUS` - URL of the Google+ page
- `SNS_TWITTER` - URL of the Twitter profile


Setup static files
------------------

You must set up Node.js in order to make static files gathering and processing
work.

1. Install Node + npm. For OS X using Homebrew: `brew install npm`
2. Install required packages: `npm install`
   `npm` will call bower after install

S3 is also supported as static server. To enable S3 support the following environment variables must be configured:

:warning: when using S3 static backend you must use Python 2, [reference](http://code.larlet.fr/django-storages/issue/155/python-3-support).

- `STATIC_BACKEND` - Set this to `s3` to enable S3 support
- `AWS_ACCESS_KEY_ID` - Your AWS access key ID
- `AWS_SECRET_ACCESS_KEY` - Your AWS secret access key
- `AWS_STORAGE_BUCKET_NAME` - Your bucket name
- `AWS_S3_CUSTOM_DOMAIN` - Optional. A custom domain to be used
