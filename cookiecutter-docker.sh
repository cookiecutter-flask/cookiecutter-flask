#!/usr/bin/env bash
set -e

PROGNAME=$0
BUILD_IMAGE=false
COOKIECUTTER_TEMPLATE='.'


usage() {
  cat << EOF >&2
Usage: $PROGNAME [OPTIONS]

Options:
-b, --build    Build Docker image before running cookiecutter
-h, --help     Show this message and exit

EOF
    exit 1
    }


process_args() {
    while test $# -gt 0
    do
      case "$1" in
          -h) usage
              ;;
          --help) usage
              ;;
          -b) BUILD_IMAGE=true
              ;;
          --build) BUILD_IMAGE=true
              ;;
          --*) usage;
              exit 1;
              ;;
          *) usage;
              exit 1;
              ;;
      esac
      shift
  done
}


run_cookiecutter() {
    if [[ "$(docker images -q cookiecutter-docker 2> /dev/null)" == "" ]] || $BUILD_IMAGE ; then
    docker build . --tag=cookiecutter-docker
    fi

    docker run -i -t -v ${PWD}:/build -w /build cookiecutter-docker ${COOKIECUTTER_TEMPLATE}
}

process_args "$@"
run_cookiecutter
