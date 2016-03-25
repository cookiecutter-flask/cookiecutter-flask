"""
Does the following:
1. Generates and saves random secret key
2. Removes the dockerfiles if docker isn't going to be used
3. Sets random passwords for the postgres service if docker is going to be used

A portion of this code was adopted from Django's standard crypto functions and
utilities, specifically:
    https://github.com/django/django/blob/master/django/utils/crypto.py
"""
import os
import random
import shutil
import sys

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

# Use the system PRNG if possible
try:
    random = random.SystemRandom()
except NotImplementedError:
    import warnings
    warnings.warn('A secure pseudo-random number generator is not available '
                  'on your system. Abort.')
    sys.exit(1)


def get_random_string(
        length=50,
        allowed_chars='abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)'):
    """
    Returns a securely generated random string.
    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits
    """
    return ''.join(random.choice(allowed_chars) for i in range(length))


def set_random_string(filepaths, string_to_replace="#RANDOM_STRING#", **random_kwargs):
    # Generate a SECRET_KEY that matches the Django standard
    random_string = get_random_string(**random_kwargs)
    print("setting random in", filepaths)
    for path in filepaths:
        with open(path, 'r') as f:
            data = f.read()
        data = data.replace(string_to_replace, random_string)
        with open(path, 'w') as f:
            f.write(data)


def remove_docker_files(path):
    """Removes all docker related files if docker isn't going to be used"""
    # Determine the local_setting_file_location
    dockerfiles = [
        ("dockerfiles", True),
        ("dev.yml", False),
        ("docker-compose.yml", False)
    ]
    for dockerfile, is_dir in dockerfiles:
        path = os.path.join(
            PROJECT_DIRECTORY,
            dockerfile,
        )
        if is_dir:
            shutil.rmtree(path=path)
        else:
            os.remove(path)

# 1. Set a random secret key in settings.py
set_random_string(
    filepaths=[os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.app_name }}', "settings.py"),],
    string_to_replace="#SECRET_KEY#",
)

# 2. Remove dockerfiles if docker isn't going to be used
if '{{ cookiecutter.use_docker }}'.lower() == 'n':
    remove_docker_files(PROJECT_DIRECTORY)

# 3. Sets random passwords for the postgres service if docker is going to be used
if '{{ cookiecutter.use_docker }}'.lower() == 'y':
    set_random_string(
        filepaths=[
            os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.app_name }}', "settings.py"),
            os.path.join(PROJECT_DIRECTORY, "dev.yml"),
            os.path.join(PROJECT_DIRECTORY, "docker-compose.yml"),
        ],
        string_to_replace="#DOCKER_POSTGRES_PASS#",
        allowed_chars='abcdefghijklmnopqrstuvwxyz0123456789!#%^&*(-_=+)'
    )
