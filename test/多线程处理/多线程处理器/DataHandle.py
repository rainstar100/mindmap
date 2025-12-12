import json

# 读取文件内容
with open('data/1.text', 'r', encoding='utf-8') as file:
    lines = file.readlines()
print(len(lines))
# 获取表头
header = lines[0].strip().split('\t')

# 初始化数据列表
data = []

# 处理每一行数据
for line in lines[1:]:
    values = line.strip().split('\t')
    if len(values) != len(header):
        values.extend(['undefined'] * (len(header)- len(values)))
    entry = {header[i]: values[i] for i in range(len(header))}
    data.append(entry)

# 将数据转换为JSON格式
print(len(data))
json_data = json.dumps(data, indent=4, ensure_ascii=False)

# 将JSON数据写入文件
with open('JSON/1.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)