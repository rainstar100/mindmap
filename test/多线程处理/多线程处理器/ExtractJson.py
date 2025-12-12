import json

# 读取JSON文件
with open('JSON/1.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# 提取特定字段
desired_fields = ['UniprotID']
filtered_data = [{field: entry[field] for field in desired_fields if field in entry} for entry in data]

# 得到UniprotID字段值所组成的字典
uniprot_ids = {entry['UniprotID'] for entry in filtered_data}
print(uniprot_ids)
# 打印提取的字段
# for entry in filtered_data:
#     print(entry)
# 修改指定记录的字段值
for entry in filtered_data:
    if entry['UniprotID'] == 'desired_uniprot_id':
        entry['UniprotID'] = 'new_value'