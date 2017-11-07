#!/usr/bin/env python
############
# Standard #
############
import os
import sys
import pytest
import logging
from logging.handlers import RotatingFileHandler

if __name__ == '__main__':
    # Show output results from every test function
    # Show the message output for skipped and expected failures
    args = ['-v', '-vrxs']

    # Add extra arguments
    if len(sys.argv) >1:
        args.extend(sys.argv[1:])

    # Setup logger and log everything to a file
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    log_filename = os.path.join(os.path.dirname(__file__), 'logs/tests.log')
    if os.path.isfile(log_filename):
        do_rollover = True
    else:
        do_rollover = False
    handler = RotatingFileHandler(log_filename, backupCount=9)
    if do_rollover:
        handler.doRollover()
    formatter = logging.Formatter(fmt=('%(asctime)s.%(msecs)03d '
                                       '%(module)-10s '
                                       '%(levelname)-8s '
                                       '%(threadName)-10s '
                                       '%(message)s'),
                                  datefmt='%H:%M:%S')
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)

    logger = logging.getLogger(__name__)
    logger.info('pytest arguments: {}'.format(args))    

    sys.exit(pytest.main(args))
