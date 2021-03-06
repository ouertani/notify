#!/usr/bin/env python

import os
from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

# notify_celery is referenced from manifest.yml, and cannot be removed
from app import notify_celery, create_app, version  # noqa

sentry_extras = dict(release=version.__commit_sha__)
sentry_extras = {opt: val for opt, val in sentry_extras.items() if val}

sentry_sdk.init(
    dsn=os.getenv("CELERY_SENTRY_DSN"),
    environment=os.getenv("CELERY_SENTRY_ENV"),
    integrations=[FlaskIntegration()],
    **sentry_extras
)

with sentry_sdk.configure_scope() as scope:
    scope.set_tag("celery_cmd", os.environ['NOTIFY_CELERY_CMD'])
    scope.set_tag("cf_app", os.environ.get('CF_APP_NAME'))

application = Flask('delivery')
create_app(application)
application.app_context().push()
