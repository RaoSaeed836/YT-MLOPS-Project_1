# below code is to check the logging config
# from src.logger import logging #  --> as kam ka ly hm na setup.pt or pyproject.toml file bnae the   
# # jb hm demo fie ko run kry gy to ya src.logger file ma ja  kr us code ko bhe run krdy g aor hmy hmare loggin file mil jay ge 
# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")

# --------------------------------------------------------------------------------

# # below code is to check the exception config
from src.logger import logging
from src.exception import MyException
import sys

try:
    a = 1+'Z'
except Exception as e:
    logging.info(e)
    raise MyException(e, sys) from e
