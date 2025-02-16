import threading
import queue
from typing import List, Callable, Any, Tuple

class MultiThreadTaskProcessor:
    def __init__(self, task_list: List[Any], task_handler: Callable[[Any], Any], num_workers: int = 4):
        """

        :param task_list: list of task。
        :param task_handler: how to  handler task。
        :param num_workers: the number of threads。
        """
        self.task_list = task_list
        self.task_handler = task_handler
        self.num_workers = num_workers
        self.task_queue = queue.Queue()
        self.result_queue = queue.Queue()
        self.exception_queue = queue.Queue()  # 异常队列
        self.workers = []

    def start(self):
        """
        start processor。
        """
        # generate task queue.
        for task in self.task_list:
            self.task_queue.put(task)

        # create threads.
        for _ in range(self.num_workers):
            worker = threading.Thread(target=self._worker)
            worker.daemon = True
            worker.start()
            self.workers.append(worker)

    def _worker(self):
        """
        workflow.
        """
        while True:
            try:
                task = self.task_queue.get_nowait()
            except queue.Empty:
                break

            try:
                result = self.task_handler(task)
                self.result_queue.put(result)
            except Exception as e:
                # add exception to exception queue
                self.exception_queue.put((task, e))
            finally:
                self.task_queue.task_done()

    def get_results(self) -> List[Any]:
        """
        get all results.
        """
        results = []
        while not self.result_queue.empty():
            results.append(self.result_queue.get())
        return results

    def get_exceptions(self) -> List[Tuple[Any, Exception]]:
        """
        get all exceptions.
        """
        exceptions = []
        while not self.exception_queue.empty():
            exceptions.append(self.exception_queue.get())
        return exceptions

    def wait_completion(self):
        """
        wait for all tasks to be completed.
        """
        self.task_queue.join()

# 示例用法
if __name__ == "__main__":
    # lsit tasks
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # task handler
    def task_handler(task: int) -> int:

        import time
        time.sleep(1)  
        if task == 3:
            raise ValueError("任务 3 处理失败")  
        return task * 2

    # create processor
    processor = MultiThreadTaskProcessor(task_list=tasks, task_handler=task_handler, num_workers=4)

    # start processor
    processor.start()

    # wait for all tasks to be completed
    processor.wait_completion()

    # get results
    results = processor.get_results()
    print("处理结果:", results)

    # get exceptions
    exceptions = processor.get_exceptions()
    print("异常信息:")
    for task, exception in exceptions:
        print(f"任务 {task} 发生异常: {exception}")