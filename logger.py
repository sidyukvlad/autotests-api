import logging

logger = logging.getLogger("AUTOTEST")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("Message DEBUG")
logger.info("Message info")
logger.warning("Message warning")
logger.error("Message error")
logger.critical("Message critical")