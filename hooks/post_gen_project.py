#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Post gen hook to ensure that the generated project
hase only one package managment, either pipenv or pip."""
import os
import shutil
import sys


def clean_extra_package_managment_files():
    """Removes either requirements files and folderor the Pipfile."""
    use_pipenv = '{{cookiecutter.use_pipenv}}'
    to_delete = []

    if use_pipenv == 'yes':
        to_delete = to_delete + ['requirements.txt', 'requirements']
    else:
        to_delete.append('Pipfile')

    try:
        for file_or_dir in to_delete:
            if os.path.isfile(file_or_dir):
                os.remove(file_or_dir)
            else:
                shutil.rmtree(file_or_dir)
        sys.exit(0)
    except OSError as e:
        sys.stdout.write(
            'While attempting to remove file(s) an error occurred'
        )
        sys.stdout.write('Error: {}'.format(e))


if __name__ == '__main__':
    clean_extra_package_managment_files()
