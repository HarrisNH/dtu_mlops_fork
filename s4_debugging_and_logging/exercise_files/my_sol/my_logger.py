from loguru import logger
import sys
## Help ensure only warnings and above are logged
logger.remove()
logger.add("my_sol/my_log.log",level="DEBUG", rotation="1 KB")
logger.add(sink = sys.stdout ,level="WARNING")

logger.critical("Critical news")
logger.error("We have hit an error")
logger.warning("Warning message")
logger.info("Extra info message")
logger.debug("Very detailed info message")

