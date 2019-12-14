import matplotlib.pyplot as plt
import numpy as np
import random

e = 2.7182818284590452353
o = 10 ** 10
gamma = 0.1

m = 10
n = 10000
t = [0] * m
t = [i for i in range(m)]  ##time
p = [0] * m  ##res
for i in range(m):  ##time
    for j in range(n):  ##num
        q = e ** (-1 * gamma * i)
        rr = random.randint(1,o)
        r = q * o
        if rr <= r:
            p[i] += 1

        #создаем кубит - матрица
        #создаем канал (гамма, матрица)

  ##iterations
            #итерация
        #меняем базис
        #измеряем r = <0p0>
    p[i] /= n

for i in range(m):
    g = - log(p[i]) / t[i]
g /= m
print(g)


plt.plot(t, p, linewidth=2.0)
plt.ylabel('Название вертикальной оси')
plt.xlabel('Название горизонтальной оси')
plt.title('название графика')