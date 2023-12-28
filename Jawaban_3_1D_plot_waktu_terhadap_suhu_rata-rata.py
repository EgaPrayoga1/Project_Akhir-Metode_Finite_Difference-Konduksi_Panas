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

# Inisialisasi array untuk menyimpan data suhu rata-rata dan waktu
average_temperatures = []
time_values = []

# Visualisasi
fig, (ax, ax_avg_temp) = plt.subplots(1, 2, figsize=(12, 5))
ax.set_xlabel("x (cm)")
pcm = ax.pcolormesh([u], cmap=plt.cm.jet, vmin=0, vmax=100)  # Plot distribusi suhu
plt.colorbar(pcm, ax=ax)
ax.set_ylim([-2, 3])  # Batas skala y

w = u.copy()  # Menyalin data suhu untuk perhitungan
counter = 0  # Inisialisasi counter
for i in range(1, node - 1):  # Melooping setiap titik grid kecuali batas
    u[i] = (dt * a * (w[i - 1] - 2 * w[i] + w[i + 1]) / dx ** 2) + w[i]  # Perhitungan suhu baru berdasarkan persamaan difusi panas
counter += dt  # Menambah waktu simulasi

# Menambahkan data untuk plot waktu vs suhu rata-rata
time_values.append(counter)
average_temperatures.append(np.mean(u))

print("t: {:.3f} s, Suhu rata-rata: {:.2f} Celcius".format(counter, np.mean(u)))
pcm.set_array([u])
ax.set_title("Distribusi Suhu pada t: {:.3f} s".format(counter))

# Melakukan iterasi untuk seluruh waktu simulasi
for _ in range(1, t_n):
    w = u.copy()  # Menyalin data suhu untuk perhitungan
    for i in range(1, node - 1):
        u[i] = (dt * a * (w[i - 1] - 2 * w[i] + w[i + 1]) / dx ** 2) + w[i]
    counter += dt

    # Menambahkan data untuk plot waktu vs suhu rata-rata
    time_values.append(counter)
    average_temperatures.append(np.mean(u))

    print("t: {:.3f} s, Suhu rata-rata: {:.2f} Celcius".format(counter, np.mean(u)))
    pcm.set_array([u])
    ax.set_title("Distribusi Suhu pada t: {:.3f} s".format(counter))

    # Update plot waktu vs suhu rata-rata
    ax_avg_temp.clear()
    ax_avg_temp.plot(time_values, average_temperatures, marker='o', linestyle='-', color='b')
    ax_avg_temp.set_xlabel('Waktu (s)')
    ax_avg_temp.set_ylabel('Suhu Rata-rata (Celcius)')
    ax_avg_temp.set_title('Waktu vs Suhu Rata-rata')
    plt.pause(0.01)  # Pause to update the plot

plt.show()
