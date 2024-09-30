from USvisa.logger import logging
from USvisa.exception import USvisaException
import sys

logging.info("Testing Custom logs ...")

try:
    a = 2/0
except Exception as e:
    raise USvisaException(e,sys)