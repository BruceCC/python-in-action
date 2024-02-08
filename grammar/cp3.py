import numpy as np
import matplotlib.pyplot as plt

# 初始化变量值
initial_principal = 10000  # 初始本金
annual_interest_rates = [0.03, 0.05, 0.07]  # 年利率列表
years = 20  # 投资年数
x_value = 15000  # x轴水平线的位置

# 创建图形
plt.figure(figsize=(10, 6))

# 循环计算并绘制每一条复利曲线
for annual_interest_rate in annual_interest_rates:
    time = np.arange(0, years+1)
    compounded_amount = initial_principal * (1 + annual_interest_rate)**time
    plt.plot(time, compounded_amount, 'o-', label=f'Interest Rate: {annual_interest_rate*100}%')

    # 计算交点并在图上进行标识
    intersection_year = np.where(np.diff(np.sign(compounded_amount - x_value)))[0]
    for intersect in intersection_year:
        plt.plot(intersect, x_value, 'go')  # 添加交点标识
        plt.text(intersect, x_value, f'   ({intersect}, {x_value})', verticalalignment='bottom')  # 添加交点坐标

# 绘制水平线
plt.axhline(y=x_value, color='r', linestyle='-', label='x line')

plt.title('Compound Interest With Horizontal Line')
plt.xlabel('Years')
plt.ylabel('Amount ($)')
plt.legend()  # 添加图例

plt.grid(True)
plt.show()
