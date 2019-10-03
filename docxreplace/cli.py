"""Search and replace word documents.
Usage:
  docxreplace <find> <replace> <file>... [options]

Options:
  -v --verbose           More messages.
  -i --ignore-case       Ignore case.
"""
import logging
import sys

from docopt import docopt

from .replace import search_replace_files

LOGGER = logging.getLogger(__name__)


class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno in (logging.DEBUG, logging.INFO)


def cli():

    arguments = docopt(__doc__)

    log_level = logging.DEBUG if arguments['--verbose'] else logging.INFO

    logger = logging.getLogger()
    logger.setLevel(log_level)

    info_handler = logging.StreamHandler(sys.stdout)
    info_handler.setLevel(log_level)
    info_handler.addFilter(InfoFilter())

    error_handler = logging.StreamHandler(sys.stderr)
    error_handler.setLevel(logging.WARNING)

    logger.addHandler(info_handler)
    logger.addHandler(error_handler)

    search_replace_files(
        arguments['<file>'],
        arguments['<find>'],
        arguments['<replace>'],
        arguments['--ignore-case']
    )
