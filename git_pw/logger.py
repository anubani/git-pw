"""
Configure application logging.
"""

import logging


def configure_verbosity(debug):  # type: (bool) -> None
    if debug:
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.ERROR, format='%(message)s')
