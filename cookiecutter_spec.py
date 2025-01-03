import argparse
from typing import List

import columbo
from cookiecutter.main import cookiecutter
from packaging.utils import canonicalize_name


def handle_cli_input():
    parser = argparse.ArgumentParser(description="Generate a cookiecutter project")
    parser.add_argument("template")
    parser.add_argument("--no-input", default=False, action="store_true")
    return parser.parse_args()


def _normalize_application_name(answers: columbo.Answers) -> str:
    application_name = str(answers.get("project_name", "example_project"))
    return application_name.lower().replace("-", "_").replace(" ", "_")


def validate_package_import_name(
    answer: str, _: columbo.Answers
) -> columbo.ValidationResponse:
    canonical_name = canonicalize_name(answer).replace("-", "_")
    if not canonical_name == answer:
        error_message = (
            "Import names should follow PEP-8 naming conventions."
            f" Did you mean {canonical_name}?"
        )
        return columbo.ValidationFailure(error=error_message)
    if not answer.replace("_", "").isalpha():
        error_message = (
            "Import names may only contain alphabetical characters and underscores. "
            "They may not contain spaces, numbers, or other characters."
        )
        return columbo.ValidationFailure(error=error_message)
    return columbo.ValidationSuccess()


interactions: List[columbo.Interaction] = [
    columbo.Echo("Please answer the following questions!"),
    columbo.BasicQuestion(
        "full_name",
        "What is your name?",
        default="First Last",
    ),
    columbo.BasicQuestion(
        "email",
        lambda answers: f"What is {answers['full_name']}'s email address?",
        default="example@gmail.com",
    ),
    columbo.BasicQuestion(
        "github_username",
        lambda answers: f"What is {answers['full_name']}'s github username?",
        default="yourGithubUsername",
    ),
    columbo.BasicQuestion(
        "project_name",
        "What is the name of your project?",
        default="My Flask App",
    ),
    columbo.BasicQuestion(
        "app_name",
        "What will the package import name be?\nThis will be the name used in python code to import from the module",
        default=_normalize_application_name,
        validator=validate_package_import_name,
    ),
    columbo.BasicQuestion(
        "project_short_description",
        "Provide a short description for the project.",
        default="A flasky app.",
    ),
    columbo.Confirm(
        "use_pipenv",
        "Should this project use pipenv?",
        default=False,
    ),
    columbo.Choice(
        "python_version",
        "Which version of Python will this application use?",
        options=["3.13", "3.12"],
        default="3.13",
    ),
    columbo.Choice(
        "node_version",
        "Which version of Node will this application use?",
        options=["22", "20"],
        default="22",
    ),
    columbo.Confirm(
        "use_heroku",
        "Will this project be deployed using heroku?",
        default=False,
    ),
]

if __name__ == "__main__":
    args = handle_cli_input()
    answers = columbo.get_answers(interactions, no_user_input=args.no_input)
    cookiecutter(args.template, no_input=True, extra_context=answers)
