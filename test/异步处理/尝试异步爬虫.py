import threading
import requests
from bs4 import BeautifulSoup

# 定义一个函数，用于抓取并解析网页标题
def fetch_title(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果响应状态码不是200，则抛出HTTPError异常
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title"
        print(f"Title from {url}: {title}")
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

# 主函数，用于启动多线程
def main():
    urls = [
        "www.baidu.com",
        "www.baidu.com",
        "www.baidu.com",
        # ... 添加更多URL
    ]

    threads = []

    # 为每个URL创建一个线程
    for url in urls:
        thread = threading.Thread(target=fetch_title, args=(url,))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print("所有页面标题抓取完成!")

if __name__ == '__main__':
    main()
