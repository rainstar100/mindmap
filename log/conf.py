# -*- encoding: utf-8 -*-
'''
@File    :   log_conf.py
@Time    :   2025/03/01 13:16:37
@Author  :   T.Student 
@Version :   1.0
@desc    :   debug log dict config 
@workflows:  logger(the setted level info )-->handler(the setted level info)-->file/console
@knowleges:  propagate represent the logger's message will be sent to the parent logger(root) or not
@usage   :   only need to change the level
'''
# here put the import lib

import logging.config as config
import logging
import conf as settings

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
        'test': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },   
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'log/file/logfile.log',
            'level': 'DEBUG',
            'formatter': 'simple',
            'encoding': 'utf-8',
        },
        'file_rotate': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/file/log_rotate.log',
            'maxBytes': 1024*1024*10, # 5 MB
            'backupCount': 30,
            'encoding': 'utf-8',
            'formatter': 'simple',
        },
    },

    'loggers': {
        'console_file': {
            'handlers': ['console','file', 'file_rotate'],
            'level': 'WARNING', #only need to change this level
            'propagate': False, 
        },
 

    },
    # root is root logger,logger_debug_conf is child logger
    'root': {
        'handlers': ['console', 'file'],
        'level': 'DEBUG',
    },
}

config.dictConfig(settings.LOGGING_CONFIG)
log_console_file = logging.getLogger('console_file')