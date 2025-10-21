# 从键盘获取输入的一行字符	
s = input()
# 初始化各类字符的计数
letter = 0
digit =0
space = 0
other = 0	
# 遍历输入的每个字符，进行分类统计
for c in s:
if c.isalpha():# 判断是否是英文字符
letter += 1
elif c.isdigit():# 判断是否是数字
digit += 1
elif c.isspace():# 判断是否是空格
space += 1
else: # 其他字符
other += 1
# 按照要求格式输出结果
 
 	print(f"英文字符:{letter}")	
 	print(f"数字: {digit}")	
print(f"空格: {space}")
print(f"其他字符:{other}")
