import threading
import queue
import requests

# 创建任务队列
task_queue = queue.Queue()

# 定义下载函数
def download(url):
    response = requests.get(url)
    # 在这里添加你的下载逻辑
    # ...

# 定义工作线程
def worker():
    while True:
        # 从任务队列中获取任务
        url = task_queue.get()
        # 执行下载任务
        download(url)
        # 标记任务完成
        task_queue.task_done()

# 创建并启动工作线程
num_workers = 4  # 设置工作线程数量
for _ in range(num_workers):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

# 添加下载任务到任务队列
urls = [
    'http://example.com/file1',
    'http://example.com/file2',
    'http://example.com/file3',
    # 添加更多的下载链接...
]

for url in urls:
    task_queue.put(url)

# 等待所有任务完成
task_queue.join()