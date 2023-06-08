import logging
from multiprocessing import Manager


state = Manager().dict()
log = logging.getLogger("log")