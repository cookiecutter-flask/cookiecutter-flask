import re
import sys


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"


class bcolors:
    WARNING = "\033[93m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


def validate_python_module_name():
    module_name = "{{ cookiecutter.app_name }}"
    if not re.match(MODULE_REGEX, module_name):
        print(
            (
                "\n{0}ERROR:{1} "
                + "{2}{3}{1} is not a valid Python module name!\n"
                + "See https://www.python.org/dev/peps/pep-0008/#package-and-module-names for naming standards.\n"
            ).format(bcolors.WARNING, bcolors.ENDC, bcolors.BOLD, module_name)
        )
        sys.exit(1)


if __name__ == "__main__":
    validate_python_module_name()
