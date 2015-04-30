#!/usr/bin/env python

import os
import logging

from flask.ext.script import Manager, Shell

from app import create_app, db
from app.models import Entry

app = create_app(os.getenv('EXFLASKR_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Entry=Entry)
manager.add_command('shell', Shell(make_context=make_shell_context))


@manager.command
def test():
    """
    Run testing procedure.
    """

    from subprocess import call
    call(['nosetests', '-v',
          '--with-coverage', '--cover-package=app', '--cover-branches',
          '--cover-erase', '--cover-html', '--cover-html-dir=cover'])


@manager.command
def initapp():
    """
    Initialize App.
    """

    db.create_all()
    logging.info('Application initialization completed successfully.')

if __name__ == '__main__':
    manager.run()
