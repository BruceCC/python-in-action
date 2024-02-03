import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 参数
principal = 100  # 初始投资金额
annual_rates = [0.01, 0.05, 0.1, 0.15]  # 年利率列表
years = np.arange(0, 30)  # 投资年数


# 计算复利
def calculate_compound_interest(principal, annual_rate, years):
    return principal * (1 + annual_rate) ** years


# 存储计算结果
values = {f'{rate * 100}%': calculate_compound_interest(principal, rate, years) for rate in annual_rates}

# 绘制复利曲线图
plt.figure(figsize=(10, 6))
for rate, value in values.items():
    plt.plot(years, value, label=rate)

one_fold_returns = 200
ten_fold_returns = 100 * 10
twenty_fold_returns = 100 * 20
plt.axhline(y=one_fold_returns, color='r', linestyle='-', label='1倍')  # 添加水平线
plt.axhline(y=ten_fold_returns, color='r', linestyle='-', label='10倍')  # 添加水平线
plt.axhline(y=twenty_fold_returns, color='r', linestyle='-', label='20倍')  # 添加水平线
plt.xlabel('Years')
plt.ylabel('Value ($)')
plt.title('Compound Interest Over Time')
plt.legend()
plt.grid(True)
plt.show()
