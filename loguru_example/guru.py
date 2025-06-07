from loguru import logger
logger.remove()  # remove all handlers
# add 新增一个日志文件handler，log.log为日志文件名,rotation参数设置日志文件大小
handler_id = logger.add("log.log", rotation="10 MB",level="ERROR")
# logger.remove(handler_id)
logger.info("info msg!")
logger.warning("warning msg!")
logger.error("error msg!")
logger.debug("debug msg!")
logger.critical("critical msg!")
