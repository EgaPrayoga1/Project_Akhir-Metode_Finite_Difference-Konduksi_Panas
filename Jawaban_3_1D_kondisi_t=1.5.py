import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan Variabel
a = 500  # Koefisien Difusivitas Termal [m^2/s]
panjang = 2.5  # Panjang plat [m]
waktu = 1.5  # Waktu simulasi [s]
node = 50  # Jumlah titik grid

dx = panjang / node  # Jarak antar titik grid [m]
dt = 0.5 * dx ** 2 / a  # Ukuran waktu simulasi [s]
t_n = int(waktu / dt)  # Jumlah iterasi simulasi
u = np.zeros(node) + 20  # Suhu awal plat [ degC ]

# Kondisi Batas
u[0] = 0  # Suhu ujung kiri plat [ degC ]
u[-1] = 100  # Suhu ujung kanan plat [ degC ]

# Visualisasi
fig, ax = plt.subplots()
ax.set_xlabel("x (cm)")
pcm = ax.pcolormesh([u], cmap=plt.cm.jet, vmin=0, vmax=100)  # Plot distribusi suhu
plt.colorbar(pcm, ax=ax)
ax.set_ylim([-2, 3])  # Batas skala y

# Simulasi
counter = 0
while counter < waktu:
    w = u.copy()  # Menyalin data suhu untuk perhitungan
    for i in range(1, node - 1):  # Melooping setiap titik grid kecuali batas
        u[i] = (dt * a * (w[i - 1] - 2 * w[i] + w[i + 1]) / dx ** 2) + w[i]  # Perhitungan suhu baru berdasarkan persamaan difusi panas

    print("t: {:.3f} s, Suhu rata-rata: {:.2f} Celcius".format(counter, np.mean(u)))
    pcm.set_array([u])
    ax.set_title("Distribusi Suhu pada t: {:.3f} s".format(counter))
    counter += dt  # Menambah waktu simulasi
    plt.pause(0.01)  # Menunda plot untuk animasi

plt.show()
