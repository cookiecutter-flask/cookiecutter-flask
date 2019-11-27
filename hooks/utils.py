class bcolors:
    WARNING = "\033[93m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


def colorize(escape_code, text):
    code = getattr(bcolors, escape_code)
    return f"{code}{text}{bcolors.ENDC}"


def log_module_name_warning(module_name, logger):
    warning = (
        f"\n{colorize('WARNING', 'WARNING:')} {colorize('BOLD', module_name)}"
        " is not a valid Python module name!\n"
        "See https://www.python.org/dev/peps/pep-0008/#package-and-module-names"
        " for naming standards.\n"
    )
    logger.warning(warning)
