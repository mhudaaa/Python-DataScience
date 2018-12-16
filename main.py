import database as db
import pandas as pd
import function as func
import numpy as np
import pymssql
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------------------
# JUMLAH AKSES SHARE ITS 5 TAHUN TERAKHIR
# ----------------------------------------------------------------------------------------------
# jmlAkses = pd.DataFrame({
#     'aksesDosen' : pd.DatetimeIndex(db.dosen['LastAccess']).year.value_counts().head(5),
#     'aksesMahasiswa' : pd.DatetimeIndex(db.mahasiswa['LastAccess']).year.value_counts().head(5),
# })
# jmlAkses['total'] = jmlAkses.aksesDosen + jmlAkses.aksesMahasiswa
# jmlAkses['total'].plot.bar(rot=0)
# plt.title('Jumlah akses Share ITS 5 tahun terakhir')
# plt.ylabel('Jumlah Akses')
# plt.xlabel('Tahun')
# for i, v in enumerate(jmlAkses['total']):
#     plt.text(i, v - 500, v, horizontalalignment='center', color='white', fontweight='bold')
# plt.show()
# ----------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------
# AKSES SHARE ITS MAHASISWA TIAP FAKULTAS PADA TAHUN 2018
# ----------------------------------------------------------------------------------------------
# data = db.mahasiswa[['Fakultas', 'LastAccess']].groupby(['Fakultas']).size().reset_index(name='Jumlah Mahasiswa')
# data = data[data['Fakultas'].str.match('Fakultas')]
#
# mhs = db.mahasiswa
# mhs['LastAccess'] = pd.DatetimeIndex(mhs['LastAccess']).year
# aks2018 = mhs[mhs['LastAccess'] == 2018].groupby(mhs['Fakultas']).size().reset_index(name='Jumlah Akses')
# aks2018 = aks2018[aks2018['Fakultas'].str.match('Fakultas')]
#
# new = pd.merge(data, aks2018, how='outer')
# #
# percent = np.round(np.array(new['Jumlah Akses']) / np.array(data['Jumlah Mahasiswa']) * 100, 1)
# new.plot.bar(rot=0)
# plt.xticks(np.arange(5), func.getAbb(new['Fakultas']))
# for i, v in enumerate(new['Jumlah Mahasiswa']):
#     plt.text(i, v+100, str(percent[i])+'%', horizontalalignment='center', color='black', fontweight='bold')
# plt.title('Akses Share ITS tiap fakultas pada tahun 2018')
# plt.xlabel('Fakultas')
# plt.show()
# ----------------------------------------------------------------------------------------------

# RATA-RATA WAKTU AKSES MAHASISWA
mhs = pd.DatetimeIndex(db.mahasiswa['LastAccess']).hour.value_counts().reset_index().sort_values('index')
waktu = pd.DataFrame({
    'waktu1' : np.sum(mhs[:6].LastAccess),
    'waktu2' : np.sum(mhs[6:12].LastAccess),
    'waktu3' : np.sum(mhs[12:18].LastAccess),
    'waktu4' : np.sum(mhs[18:24].LastAccess)
}, index=[0])
print(waktu)