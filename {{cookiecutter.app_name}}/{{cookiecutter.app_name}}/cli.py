# -*- coding: utf-8 -*-
"""Click commands."""
import click
import os
from flask.cli import with_appcontext

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)
TEST_PATH = os.path.join(PROJECT_ROOT, 'tests')


@click.command('test')
@with_appcontext
def test_command():
    """Run the tests."""
    import pytest
    pytest.main([TEST_PATH, '--verbose'])
