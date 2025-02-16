#queue.py导致循环导入
import queue
import threading
import time
import requests

#get entry ids 
def get_entry_ids():

    # ask SABIO-RK for all EntryIDs matching a query
    query_dict = {"ECNumber":"*"}
    query_string = ' AND '.join(['%s:%s' % (k,v) for k,v in query_dict.items()])
    query = {'format':'txt', 'q':query_string}
    url = "https://sabiork.h-its.org/sabioRestWebServices/searchKineticLaws/entryIDs"
    response = requests.post(url, data=query)
    response.raise_for_status()
    print(f"{response.status_code} success!!!")
    EntryIDs=response.text.strip().split('\n') #[]set numbers for debug
    #print(f"EntryIDs: {EntryIDs} are downloaded")
    return EntryIDs

#generate tasks queue
def generate_tasks_queue(EntryIDs,entryIDSNums):

    q=queue.Queue(maxsize=entryIDSNums)
    for EntryID in EntryIDs:
        q.put(EntryID)
    return q


def generate_error_tasks_queue(entryIDSNums):
    q=queue.Queue(maxsize=entryIDSNums)
    return q

def downloader(EntryID):
    kcat_url='http://sabiork.h-its.org/entry/exportToExcelCustomizable'
    data_field = {'entryIDs[]': EntryID}
    fields=['Buffer', 'Cofactor', 'ECNumber', 'EntryID', 'Organism', 'Product', 'PubMedID', 'SabioCompoundID', 'SabioReactionID', 'Substrate', 'Temperature', 'UniprotID', 'Unit', 'Value', 'pH']
    query={
                    'format':'tsv',
                    'fields[]':fields
            }
    response = requests.post(kcat_url, params=query, data=data_field)

    #check response
    try:
        response.raise_for_status()
    except Exception as e:
        print(f"{EntryID} is failed---{response.status_code}")
        error_queue.put(EntryID+"--->"+str(response.status_code))
        return None
    else:
        print(f"{EntryID} is downloaded---{response.status_code}--->{len(response.text)}")
        return response.text
#handle data
def handle_data(data):
    rows=data.split('\n')
    print(rows)
    # print(rows[0].split('\t'))
    # for row in rows[1:-1]:
    #     row=row.split('\t')
    #     if  row[6]=="kcat":
    #         print('==================')
    #         print(row)


def worker(task_queue,error_queue):
    while not task_queue.empty():

        EntryID=task_queue.get()
        #get response for downloader
        data=downloader(EntryID)
        if data:
            handle_data(data)

        task_queue.task_done()

# for item in range(10):
#     q.put(item)



if __name__ == "__main__":
    EntryIDS=get_entry_ids()[:10]
    entryIDSNums=len(EntryIDS)
    tasks_queue=generate_tasks_queue(EntryIDS,entryIDSNums)
    print(f"tasks_numbers: {tasks_queue.qsize()}")
    error_queue=generate_error_tasks_queue(entryIDSNums)
    print(f"error_queue_numbers: {error_queue.qsize()}")

    theads=[]
    for t in range(100):
        theads.append(threading.Thread(target=worker,args=(tasks_queue,error_queue)))
        theads[-1].start()

    tasks_queue.join()

    for t in theads:
        t.join()
    
