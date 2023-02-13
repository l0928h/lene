#
#
import matplotlib.pyplot as plt
w = []
s = []
y = []
z = []

plt.plot(x, y, lw=2, label='Len')
plt.plot(w, z, lw=2, label='Raymond')
plt.xlabel('month')
plt.ylabel('dollars (million)')
plt.legend()
plt.title('Program Mooji')
plt.show()
