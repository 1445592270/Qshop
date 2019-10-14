import logging

logging_hander=logging.FileHandler('test.log',encoding='utf-8')
stream_hander=logging.StreamHandler()
log_format='%(asctime)s【%(levelname)s】%(message)s'
time_format='%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.DEBUG,format=log_format,datefmt=time_format,handlers=[logging_hander,stream_hander])
logging.debug('this level is debug ')
logging.info('this level is info ')
logging.warning('this level is warning ')
logging.error('this level is error ')
logging.critical('this level is critical ')







