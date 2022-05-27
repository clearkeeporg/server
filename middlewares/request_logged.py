import logging
logger = logging.getLogger(__name__)

def request_logged(func):
    async def deco(*args, **kwargs):
        # Before request handlers
        print("Request Object Type=", type(args[1]).__name__)
        print(args[1])
        logger.info("Request Object Type=" + type(args[1]).__name__)
        logger.info(args[1])
        return await func(*args, **kwargs)

    return deco
