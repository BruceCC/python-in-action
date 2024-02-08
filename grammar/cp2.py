import numpy as np
import matplotlib.pyplot as plt

# 初始化变量值
initial_principal = 10000  # 初始本金
annual_interest_rate = 0.05  # 年利率
years = 20  # 投资年数
x_value = 20000  # x 需要画出的水平线的值

# 计算复利
time = np.arange(0, years+1)
compounded_amount = initial_principal * (1 + annual_interest_rate)**time

# 创建复利曲线图
plt.figure(figsize=(10,5))
plt.plot(time, compounded_amount, 'o-', label='Compound Interest')
plt.axhline(y=x_value, color='r', linestyle='-', label='x line')  # 添加水平线

# 计算交点并在图上进行标识
intersection_year = np.where(np.diff(np.sign(compounded_amount - x_value)))[0]
for intersect in intersection_year:
    plt.plot(intersect, x_value, 'go')  # 添加交点标识
    plt.text(intersect, x_value, f'   ({intersect}, {x_value})', verticalalignment='bottom')  # 添加交点坐标

plt.title('Compound Interest With Horizontal Line')
plt.xlabel('Years')
plt.ylabel('Amount ($)')
plt.legend()  # 添加图例

plt.grid(True)
plt.show()
