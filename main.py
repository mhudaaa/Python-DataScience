import database as db
import pandas as pd
import function as func
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------------------
# JUMLAH AKSES SHARE ITS 5 TAHUN TERAKHIR
# ----------------------------------------------------------------------------------------------
"""
# --- Akses Dosen & Mahasiswa
akses = pd.DataFrame({
    'AksesDosen' : pd.DatetimeIndex(db.dosen['LastAccess']).year.value_counts().head(5),
    'AksesMahasiswa' : pd.DatetimeIndex(db.mahasiswa['LastAccess']).year.value_counts().head(5),
})
akses.plot.bar(rot=0)
plt.yticks(np.arange(0, 16000, 2000))
func.setPlotText(akses.AksesDosen, x=-0.05, y=300, color='#1F77B4')
func.setPlotText(akses.AksesMahasiswa, x=0.1, y=200, halign='center', color='#FF7F0E')
func.showPlot(title='Akses Share ITS Dosen & Mahasiswa 5 tahun terakhir', xlabel='Tahun', ylabel='Jumlah Akses')

# --- Total Akses
totalAkses = akses.AksesDosen + akses.AksesMahasiswa
totalAkses.plot.bar(rot=0)
func.setPlotText(totalAkses, x=0, y=100, halign='center')
plt.yticks(np.arange(0, 14000, 2000))
func.showPlot(title='Jumlah akses Share ITS 5 tahun terakhir', xlabel='Tahun', ylabel='Jumlah Akses')
plt.show()
"""
# ----------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------
# AKSES SHARE ITS MAHASISWA TIAP FAKULTAS PADA TAHUN 2018
# ----------------------------------------------------------------------------------------------
# Get Jumlah Mahasiswa
jmlMhs = db.mahasiswa[['Fakultas', 'LastAccess']].groupby(['Fakultas']).size().reset_index(name='Jumlah Mahasiswa')
jmlMhs = jmlMhs[jmlMhs['Fakultas'].str.match('Fakultas')]

# Get Jumlah Akses Mahasiswa
mhs = db.mahasiswa
mhs['LastAccess'] = pd.DatetimeIndex(mhs['LastAccess']).year
jmlAkses = mhs[mhs['LastAccess'] == 2018].groupby(mhs['Fakultas']).size().reset_index(name='Jumlah Akses')
jmlAkses = jmlAkses[jmlAkses['Fakultas'].str.match('Fakultas')]

# Merge Jumlah Mahasiswa & Jumlah Akses
jmlAksesMhs = pd.merge(jmlMhs, jmlAkses, how='outer')

# Set Plot
jmlAksesMhs.plot.bar(rot=0)
plt.xticks(np.arange(5), func.getAbb(jmlAksesMhs['Fakultas']))
plt.yticks(np.arange(0, 12000, 2000))

# Set Plot Text
func.setPlotText(jmlAksesMhs['Jumlah Mahasiswa'], x=0, y=200, color='#1F77B4')
func.setPlotText(jmlAksesMhs['Jumlah Akses'], x=0.05, y=200, halign='left', color='#FF7F0E')

# Show Plot
func.showPlot(title='Akses Share ITS Mahasiswa tiap fakultas pada tahun 2018', xlabel='Fakultas')

percent = pd.DataFrame({
    'Fakultas' : func.getAbb(jmlAksesMhs['Fakultas']),
    'Akses' : np.round(np.array(jmlAksesMhs['Jumlah Akses']) / np.array(jmlAksesMhs['Jumlah Mahasiswa']) * 100, 1),
})
percent.plot.bar(rot=0)
func.setPlotText(percent['Akses'], x=0, y=1, val='%', halign='center')

# Set ticks
plt.yticks(np.arange(0, 140, 20))
plt.xticks(np.arange(5), percent['Fakultas'])
func.showPlot(title='Persentase akses Share ITS Mahasiswa pada tahun 2018', xlabel='Fakultas', ylabel='Akses (%)')
# ----------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------
# RATA-RATA WAKTU AKSES MAHASISWA
# ----------------------------------------------------------------------------------------------
"""
mhs = pd.DatetimeIndex(db.mahasiswa['LastAccess']).hour.value_counts().reset_index().sort_values('index')
waktuAkses = pd.DataFrame({
    'waktu' : ['00:00 - 05:59', '06:00 - 11:59', '12:00 - 17:59', '18:00 - 23:59'],
    'jumlah' : [np.sum(mhs[:6].LastAccess), np.sum(mhs[6:12].LastAccess), np.sum(mhs[12:18].LastAccess), np.sum(mhs[18:24].LastAccess)]
})
waktuAkses.plot.bar(rot=0)
for i, v in enumerate(waktuAkses['jumlah']):
    plt.text(i, v-500, v, horizontalalignment='center', color='white', fontweight='bold')
plt.xticks(np.arange(4), waktuAkses['waktu'])
plt.ylabel('Jumlah Akses')
plt.xlabel('Waktu Akses')
plt.show()
"""
# ----------------------------------------------------------------------------------------------
