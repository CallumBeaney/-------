# 导入必要的模块
import os

# 打开文件以进行读写
file_path = 'example.txt'
with open(file_path, 'w', encoding='utf-8') as file:
    # 写入文本内容
    file.write('这是一个示例文本文件。\n')
    file.write('第二行文本。\n')

# 检查文件是否存在
if os.path.exists(file_path):
    # 打开文件以进行读取
    with open(file_path, 'r', encoding='utf-8') as file:
        # 读取文件内容
        file_content = file.read()
        print('文件内容：\n', file_content)
else:
    print('文件不存在！')
