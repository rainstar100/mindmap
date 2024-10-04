
############不能有返回值，但是可以定义一个顶层变量，来接收返回值

import threading
import time



# 定义一个函数，用于抓取并解析网页标题
def fetch_title(url,results):

    print(url)
    time.sleep(1)
    results.append(url*2)
# 主函数，用于启动多线程
def main():
    results=[]
    urls = [1,2,3,4,5,6,7,8,9,10
    ]
    #同步
    # for url in urls:
    #     fetch_title(url,results)
    # threads = []

    # 为每个URL创建一个线程
    for url in urls:
        thread = threading.Thread(target=fetch_title, args=(url,results))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print("所有页面标题抓取完成!")

    print(results)

if __name__ == '__main__':
    main()
