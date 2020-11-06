import matplotlib.pyplot as plt
import seaborn as snspackage control: inst
from matplotlib import rc
rc('text', usetex=True)


path = "ej22monte2.txt"
f = []
mag = []


bw = []
fa = []


input = open(path, "r")

line = input.readline()  # descarto la linea
line = input.readline()

while len(line):  # solo se devuelve vacio si llegue al EOF
    while len(line):
        if not line[0].isdigit():
            break
        freq, line = line.split("\t(", 1)
        f.append(float(freq))
        m, line = line.split('d', 1)
        mag.append(float(m))
        line = input.readline()

    a = next((m for m in mag if m > 5), None)
    if a is not None:
        bw.append(f[mag.index(a)])

    for i in range(len(mag)):
        if mag[len(mag)-1-i] > 5:
            bw.append(f[len(mag)-1-i])




    f.clear()
    mag.clear()

    line = input.readline()


fig = sns.distplot(bw)
y_vals = fig.get_yticks()
sum = 0
for i in y_vals:
    sum += i
factor = 1/sum
fig.set_yticklabels(['{:3.0f}%'.format(x * factor * 100) for x in y_vals])

#plt.savefig("histograma_marce.png")
plt.title('Ancho de banda')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Probabilidad')
plt.grid(True)
plt.show()

fig = sns.distplot(fa)
y_vals = fig.get_yticks()
sum = 0
for i in y_vals:
    sum += i
factor = 1/sum
fig.set_yticklabels(['{:3.0f}%'.format(x * factor * 100) for x in y_vals])

#plt.savefig("histograma_marce.png")
plt.title('Frecuencia de banda atenuada')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Probabilidad')
plt.grid(True)
plt.show()
#
#
# fig = sns.distplot(f2)
# y_vals = fig.get_yticks()
# sum = 0
# for i in y_vals:
#     sum += i
# factor = 1/sum
# fig.set_yticklabels(['{:3.0f}%'.format(x * factor * 100) for x in y_vals])
#
# #plt.savefig("histograma_marce.png")
# plt.title('Polo segunda etapa')
# plt.xlabel('Frecuencia (Hz)')
# plt.ylabel('Probabilidad')
# plt.grid(True)
# plt.show()
#
#
# fig = sns.distplot(f3)
# y_vals = fig.get_yticks()
# sum = 0
# for i in y_vals:
#     sum += i
# factor = 1/sum
# fig.set_yticklabels(['{:3.0f}%'.format(x * factor * 100) for x in y_vals])
#
# #plt.savefig("histograma_marce.png")
# plt.title('Polo tercera etapa')
# plt.xlabel('Frecuencia (Hz)')
# plt.ylabel('Probabilidad')
# plt.grid(True)
# plt.show()
# # n, bins, _ = plt.hist(bw)
# # plt.xlabel('Frecuencia (Hz)')
# # plt.ylabel('Probabilidad')
# # plt.grid(True)
# # plt.show()
# #
# #
# # n, bins, _ = plt.hist(f1)
# # plt.xlabel('Frecuencia (Hz)')
# # plt.ylabel('Probabilidad')
# # plt.grid(True)
# # plt.show()
# #
# # n, bins, _ = plt.hist(f2)
# # plt.xlabel('Frecuencia (Hz)')
# # plt.ylabel('Probabilidad')
# # plt.grid(True)
# # plt.show()
# #
# #
# # n, bins, _ = plt.hist(f3)
# # plt.xlabel('Frecuencia (Hz)')
# # plt.ylabel('Probabilidad')
# # plt.grid(True)
# # plt.show()
