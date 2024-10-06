    
import os 
'''
在f-string中，字符串前面有一个f或F前缀，并且在大括号{}内可以包含任何有效的Python表达式。这些表达式在运行时会被求值，并且其结果会被转换成字符串（如果它们不是字符串的话），然后插入到包含它们的字符串中。
'''
print(f"Process ID: {os.getpid()}") 
b=b'hello' 
print(b)
r=r'hello\n' #原始字符串，打印时\n不会转义成回车
print(f'have r---{r}')
no_r='hello\n'
print(f'no_r---{no_r}')

#字符串 ，就是unicode字符串，我们通常有字符串，文本等
b='hello'
print(f'i am string {b}')
#字节字符串
print(f'i am bytes {b.encode()}')

#字节字符串的例子
# 打开二进制文件进行读取  
with open('./字符串处理/example.png', 'rb') as file:  
    # 读取文件内容到字节字符串中  
    byte_data = file.read()  
  
# 打印文件内容的字节大小  
print(f"File size in bytes: {len(byte_data)}")  
  
# 如果你想查看文件内容的前几个字节（例如前10个字节），可以这样做：  
print(f'i am byts string {byte_data[:10]}')
print(f'i am string {b'hello'.decode()}')

'''
字符串用encode()编码成字节字符串
字节字符成用decode()解码成字符串
字节字符串是PYTHON数据类型，用于表示和处理二进制数据，就是python里的二进制字节字符串形式。
二进制字节字符串是计算机概念，表示图像，可执行程序等
'''