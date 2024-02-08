
# 使用*解包序列或可迭代对象
# https://blog.csdn.net/m0_48891301/article/details/134004143

# 示例：传递可变数量的参数
def sum_values(*args):
    total = 0
    for num in args:
        total += num
    return total
result = sum_values(1, 2, 3, 4, 5)
print(result)  # 输出：15
# 示例：拼接列表
numbers = [1, 2, 3, 4, 5]
result = [*numbers, 6, 7, 8]
print(result)  # 输出：[1, 2, 3, 4, 5, 6, 7, 8]

# 使用**解包字典
# 示例1：传递可变数量的关键字参数
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
print_info(name="Alice", age=25, city="New York")
# 输出：
# name : Alice
# age : 25
# city : New York

# 示例：拼接字典
defaults = {"color": "red", "size": "medium"}
user_preferences = {"size": "large", "theme": "dark"}
result = {**defaults, **user_preferences}
print(result)
# 输出：{'color': 'red', 'size': 'large', 'theme': 'dark'}
