import matplotlib.pyplot as plt
import numpy as np
import cirq

measure_density_matrix(density_matrix, indices)

Performs a measurement of the density matrix in the computational basis.

cirq.single_qubit_matrix_to_gates(mat: numpy.ndarray, tolerance: float = 0) → List[cirq.ops.gate_features.SingleQubitGate]
qubit = cirq.GridQubit(0, 0)
cirquit cirq.Circuit()
cirq.phase_damp(gamma: float)()

condition = [[0,1], [0,1]]
gamma = 10

t = [0] * m
n = 10000
t = [i for i in range(n)]  ##time
p = [0] * m  ##res
for i in range(m):  ##time
    for j in range(n):  ##num
        #создаем кубит - матрица
        #создаем канал (гамма, матрица)
        for k in range(t[i]):  ##iterations
            #итерация
        #меняем базис
        #измеряем r = <0p0>
        if r == 0:
            p[i] += 1
    p[i] /= n

for i in range(m):
    g = - log(p[i]) / t[i]
g /= m
print(g)


plt.plot(t, p, linewidth=2.0)
plt.ylabel('Название вертикальной оси')
plt.xlabel('Название горизонтальной оси')
plt.title('название графика')