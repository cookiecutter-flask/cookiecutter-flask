import logging
import re
import sys

LOGGER = logging.getLogger()
MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"


class bcolors:
    WARNING = "\033[93m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


def colorize(escape_code, text):
    code = getattr(bcolors, escape_code)
    return f"{code}{text}{bcolors.ENDC}"


def log_warning(module_name):
    warning = (
        f"\n{colorize('WARNING', 'WARNING:')} {colorize('BOLD', module_name)}"
        " is not a valid Python module name!\n"
        "See https://www.python.org/dev/peps/pep-0008/#package-and-module-names"
        " for naming standards.\n"
    )
    LOGGER.warning(warning)


def validate_python_module_name():
    module_name = "{{ cookiecutter.app_name }}"
    if not re.match(MODULE_REGEX, module_name):
        log_warning(module_name)
        sys.exit(1)


if __name__ == "__main__":
    validate_python_module_name()
