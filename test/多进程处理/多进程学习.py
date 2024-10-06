import multiprocessing
from bs4 import BeautifulSoup

# 假设这是你的文档处理函数
def process_document(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    # 在这里进行你的文档处理逻辑
    # ...
    return soup.prettify()  # 例如，返回文档的美化版本


if __name__ == '__main__':  
    #确保在可执行文件里多进程能正确执行
    multiprocessing.freeze_support() 
# 假设你有一个文档列表
    documents = [
        "<html><body><p>Document 1</p></body></html>",
        "<html><body><p>Document 2</p></body></html>",
        "<html><body><p>Document 3</p></body></html>",
        "<html><body><p>Document 4</p></body></html>",
        # ... 更多文档
    ]

    # create a pool that means create processes of process whoes status is inital
    #pool = multiprocessing.Pool(processes=4)  # 假设你想要使用4个进程
    pool=multiprocessing.Pool(processes=4) 

    # 使用进程池来异步处理文档
    #results = [pool.apply_async(process_document, (doc,)) for doc in documents]
    # set a list to restore the result of process
    results=[]
    for doc in documents:
        result=pool.apply_async(process_document,(doc,)) #asyn submit task to process in pool
        results.append(result)

    # 等待所有进程完成，并收集结果
    processed_documents = [result.get() for result in results]

    # 输出处理后的文档
    for doc in processed_documents:
        print(doc,'---------')

    # 关闭进程池
    pool.close()
    pool.join()

   
