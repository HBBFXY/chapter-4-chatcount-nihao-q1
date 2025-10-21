s = input()
letter = 0
digit =0
space = 0
other = 0	
for c in s:
 if c.is alpha():
  letter += 1
 elif c.is digit():
  digit += 1
 elif c.is space():
  space += 1
 else:
  other += 1
print(f"英文2字符:{letter}")	
print(f"数字:{digit}")	
print(f"空格:{space}")
print(f"其他字符:{other}")
