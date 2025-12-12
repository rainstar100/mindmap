# -*- encoding: utf-8 -*-
'''
@File    :   内存泄漏.py
@Time    :   2025/03/02 19:44:15
@Author  :   T.Student 
@Version :   1.0
@desc    :   you can put some description here
workflows:   work1 -> work2 -> work3
'''

# here put the import lib
import time
from concurrent.futures import Future

class ExecutorWithoutFinally:
    def submit(self, fn, *args, **kwargs):
        future = Future()
        try:
            result = fn(*args, **kwargs)
            future.set_result(result)
        except Exception as e:
            future.set_exception(e)
        return future

    def map(self, fn, *iterables, timeout=None, chunksize=1):
        if timeout is not None:
            end_time = timeout + time.monotonic()

        fs = [self.submit(fn, *args) for args in zip(*iterables)]

        def result_iterator():
            # 没有 finally 块
            fs.reverse()
            while fs:
                if timeout is None:
                    yield self._result_or_cancel(fs.pop())
                else:
                    yield self._result_or_cancel(fs.pop(), end_time - time.monotonic())

        return result_iterator()

    def _result_or_cancel(self, future, timeout=None):
        try:
            if timeout is None:
                return future.result()
            else:
                return future.result(timeout=timeout)
        except Exception as e:
            future.cancel()
            raise e

# 示例函数
def example_function(x):
    if x == 2:
        raise ValueError("Example exception")
    return x * 2

# 使用示例
executor = ExecutorWithoutFinally()
iterables = [1, 2, 3]
result_iter = executor.map(example_function, iterables)

try:
    for result in result_iter:
        print(result)
except Exception as e:
    print(f"Exception caught: {e}")

# 检查未完成的 Future 对象
for future in executor.map(example_function, iterables):
    if not future.done():
        print("Future not done:", future)