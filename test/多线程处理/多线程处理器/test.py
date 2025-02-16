from MultiTaskProcessor import MultiThreadTaskProcessor as mttp
import requests

tasks = [1,2]

def task_handler(task):

    PARAM_QUERY_URL = 'https://sabiork.h-its.org/entry/exportToExcelCustomizable'

    # encode next request, for parameter data given entry IDs

    data_field = {'entryIDs[]':task}
    fields=['Buffer', 'Cofactor', 'ECNumber', 'EntryID','Parameter','Organism', 'Product', 'PubMedID', 'SabioCompoundID', 'SabioReactionID', 'Substrate', 'Temperature', 'UniprotID', 'Unit', 'Value', 'pH']
    query = {'format':'tsv', 'fields[]':fields[:-3]}

    request = requests.post(PARAM_QUERY_URL, params=query, data=data_field)
    request.raise_for_status()

    return request.text

# create processor
processor = mttp(task_list=tasks, task_handler=task_handler, num_workers=4)

# start processor
processor.start()

# wait for all tasks to be completed
processor.wait_completion()
# get results
results = processor.get_results()
print("处理结果:", results[0])

# get exceptions
exceptions = processor.get_exceptions()
print("异常信息:")
for task, exception in exceptions:
    print(f"任务 {task} 发生异常: {exception}")


