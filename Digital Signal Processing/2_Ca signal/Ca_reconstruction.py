import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# 初始参数设定
K = 2
variance = 0.1
N = 1000
n = np.arange(0, N)

# 输入信号
input = np.zeros(N)
input[100], input[240], input[280], input[360], input[400] = 1, 1, 1, 1, 1

# 卷积模板
template = 0.5*np.exp(-(np.linspace(0, 10, N)))

# 输出信号
output = np.zeros(len(input) + len(template) - 1)  # shape: (1999, )

# 卷积运算
for i in range(len(input)):
    output[i:i + len(template)] = output[i:i + len(template)] + input[i]*template
# output = output[:N]

# 叠加噪声
noise = np.random.normal(0, variance, len(output))
output = output + noise

# 重建信号
T = len(template)
column = np.zeros(T + N - 1)
column[0:T] = template
Ah = []
for i in range(len(input)):
    col_i = np.concatenate((column[(len(column) - i) : len(column)], column[0:(len(column) - i)]))
    Ah.append(col_i)
Ah = np.stack(Ah, axis = 1)  # shape: (1999, 1000)

def f_loss(X):
    v = lambda X: np.sum(np.sum((np.matmul(Ah, X) - output)**2) + K*np.sum(np.abs(X)))
    return v

re_init = np.zeros(1000)
# re_init = np.random.rand(1000)
re = input
for i in range(400, 1000):
    re_init[i] = 0
for i in range(90):
    re_init[i] = 0    
re_input = minimize(f_loss(re_init), (re_init), method='SLSQP')
print(re_input.fun)
print(re_input.success)
print(re_input.x.shape)


# 作图
ax1 = plt.subplot(4, 1, 1) # 4行1列，位置是1的子图
ax1.set_title("original signal")
plt.plot(n, input, 'r')
plt.ylabel('input')

ax2 = plt.subplot(4, 1, 2)
ax2.set_title("template")
plt.plot(n, template, 'r')
plt.ylabel('t')

# ax3 = plt.subplot(4, 1, 3)
# ax3.set_title("original Ca signal")
# plt.plot(n, output[:N], 'r')
# plt.ylabel('output')

ax3 = plt.subplot(4, 1, 3)
ax3.set_title("noisy Ca signal")
plt.plot(n, output[:N], 'r')
plt.ylabel('Ca signal')

ax4 = plt.subplot(4, 1, 4)
ax4.set_title("reconstruction")
plt.plot(n, re_input.x, 'r')
plt.ylabel('reconstructed signal')

plt.tight_layout() 
plt.show()