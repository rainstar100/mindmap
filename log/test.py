# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2025/03/01 13:46:59
@Author  :   T.Student 
@Version :   1.0
@desc    :   this is a test/usecase file for logging config dictionary
workflows:   as the code
@note    :   !!!only need to change the importing path of the conf file!!!
'''

# here put the import lib

from conf import log_console_file as mylog

if __name__ == '__main__':


    mylog.debug('This is a debug message')
    mylog.info('This is an info message')
    mylog.warning('This is a warning message')
    mylog.error('This is an error message')
    mylog.critical('This is a critical message')

