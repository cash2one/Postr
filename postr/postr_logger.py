import logging
import logging.config
import errno
import datetime
import os
import sys
from postr.git_tools import git_root_dir


debug_level = logging.INFO
ROOT_DIR = git_root_dir()
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def make_log_path(log_path: str) -> None:
    if not os.path.exists(log_path):
        try:
            os.makedirs(log_path)
        except OSError as exc:  # Lack of permissions
            if exc.errno != errno.EEXIST:
                raise exc


def make_logger(name: str) -> logging.Logger:
    log_path = os.path.join(ROOT_DIR, 'logs', name)
    make_log_path(log_path)

    now = str(datetime.datetime.now()).replace(':', '-').replace(' ', '_')
    filename = os.path.join(log_path, f'{name}-{now}.log')

    logging.basicConfig(format=LOG_FORMAT, filename=filename, level=logging.DEBUG)
    logger = logging.getLogger(name)
    logger.setLevel(debug_level)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(LOG_FORMAT)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger
