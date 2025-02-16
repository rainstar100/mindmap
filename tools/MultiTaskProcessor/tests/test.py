# tests/test_processor.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from MultiTaskProcessor import MultiThreadTaskProcessor as mttp
    
    
# lsit tasks
tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# task handler
def task_handler(task: int) -> int:

        import time
        time.sleep(1)  
        if task == 3:
            raise ValueError("failed to process task 3")  
        return task * 2

# create processor
processor = mttp(task_list=tasks, task_handler=task_handler, num_workers=4)

    # start processor
processor.start()

    # wait for all tasks to be completed
processor.wait_completion()

    # get results
results = processor.get_results()
print("results:", results)

    # get exceptions
exceptions = processor.get_exceptions()
print("exception:")
for task, exception in exceptions:
    print(f"【{task}】 occor: {exception}")