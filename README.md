# Tucil2_13520012

## Deskripsi Program
Program ini adalah program yang dapat mencari convex hull dari sebuah dataset

## Requirement
1. Python
2. Library/module yang ada di requirements.txt

## Cara menjalankan
1. Clone repository ini
2. Jika ada library/module dalam requirements.txt yang belum terinstall, jalankan
``` python
pip install -r requirements.txt
```
3. Cd ke /src
4. Buka main.ipynb dan run kode per "kotak" dari atas sampai bawah
5. Jika ingin mencoba atribut(kolom) lain, pada kode yang seperti
``` python
⋅⋅⋅plt.title(str(data.feature_names[0]) + " vs " + str(data.feature_names[1]))
⋅⋅⋅plt.xlabel(data.feature_names[0])
⋅⋅⋅plt.ylabel(data.feature_names[1])
```
⋅⋅⋅dan
``` python
⋅⋅⋅bucket = bucket.iloc[:,[0,1]].values
```
⋅⋅⋅Angka 0 dan 1 bisa diganti dengan angka kolom lain.
Di tempat angka 0, semua angkanya harus sama, begitu pula di tempat angka 1

## Pembuat
Aji Andhika Falah   13520012
