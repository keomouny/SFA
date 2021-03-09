import logging
import os

logging.basicConfig(filename=f"{os.getcwd()}/logs/log.log",filemode="a", format="%(asctime)s - %(levelname)-8s - %(message)s", datefmt="%d/%m/%Y %H:%M:%S", level=logging.DEBUG)

logger = logging.getLogger(__name__)
