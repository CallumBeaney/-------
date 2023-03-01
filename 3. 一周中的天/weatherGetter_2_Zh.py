import datetime

# 获取当前日期和时间
now = datetime.datetime.now()

# 获取星期几的整数值（星期一为0，星期天为6）
day_of_week = now.weekday()

# 将整数值转换为星期几的字符串表示
days = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
day_name = days[day_of_week]

# 输出星期几
print("今天是", day_name)

# 这个程序使用Python的datetime模块获取当前日期和时间。然后，它使用weekday()方法获取星期几的整数值，其中星期一为0，星期天为6。最后，它使用一个包含星期名称的列表将整数值转换为星期几的字符串表示，并将结果打印出来。