import json  
  
# 要写入的数据  
data1= {  
    "name": "Bob",  
    "age": 25,  
    "city": "San Francisco",  
    "skills": ["JavaScript", "React", "Node.js"]  
}  

data2= {  
    "name": "Bob",  
    "age": 25,  
    "city": "San Francisco",  
    "skills": ["JavaScript", "React", "Node.js"]  
} 

data3= {  
    "name": "Bob",  
    "age": 25,  
    "city": "San Francisco",  
    "skills": ["JavaScript", "React", "Node.js"]  
} 
# 写入JSON文件  
with open('./json处理/output.json', 'w', encoding='utf-8') as file:  
    file.write("[\n")
    json.dump(data1, file, ensure_ascii=False, indent=4)
    file.write(",\n")
    json.dump(data2, file, ensure_ascii=False, indent=4)  
    file.write(",\n")
    json.dump(data2, file, ensure_ascii=False, indent=4)  
    file.write(",\n]")
print("数据已写入 output.json")