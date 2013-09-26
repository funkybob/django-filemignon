#!/usr/bin/env python

import os, sys
from django.conf import settings
from django.core.files.storage import Storage

DIRNAME = os.path.dirname(__file__)
settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    DATABASE_NAME=os.path.join('database.db'),
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'filemignon',
        'filemignon.tests',),
    FILEMIGNON_STORAGE=Storage(),)


from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)

failures = test_runner.run_tests(['filemignon',])
if failures:
    sys.exit(failures)
