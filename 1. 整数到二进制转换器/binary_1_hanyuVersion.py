# 要将整数转换为二进制，请从所讨论的整数开始并将其除以 2，注意商和余数。 
# 继续将商除以 2，直到商为零。 然后以相反的顺序写出余数。

# ("def" = "定义")
def 反转字符串(字符串):     # 句法: 函数名(传入函数的变量)
    return 字符串[::-1]   # 现在不用担心这个语法

# "="   给选的变量一个值, "=="  给确认是否选的变量和其他的有同值

用户输入 = input('请给我整数： ')  # input()  = 问收输入 
用户整数 = int(用户输入)          # int()    = 把某个变量变化转变整数

二进制数字 = "" 
# 这是一个“字符串”。 “字符串”由“字符”组成
# 因为我们使用的是“字符串”，所以我们可以这样添加：["1" + "1" = "11"] 而不是 [1 + 1 = 2]

# Python 可能会尝试将此变量视为十进制数。 我们使用 int() 强制 Python 将此变量视为整数，即整数。
while (int(用户整数) >= 1):
    余 = 用户整数 % 2             # % 得到一个除法的余数
    if 余 == 1:
      二进制数字 += "1"           # [二进制数字 = 二进制数字 + "1"] 和一样
    else: 
      # 余 == 0
      二进制数字 += "0"
    
    用户整数 = int(用户整数 / 2)    # / 得到除法的结果

二进制数字的反转 = 反转字符串(二进制数字)
print(二进制数字的反转) # print() = 打印(传入函数的变量)

# 12    应该是           1100
# 4435  应该是  1000101010011
