print("===TUTOR KA RICK===")
# operasi aritmatika

# Mendefinisikan variable
angka1 = 10
angka2 = 5
angka3 = 1

# Operasi penjumlahan
hasil_penjumlahan = angka1 + angka2 + angka3
print("Hasil penjumlahan:", hasil_penjumlahan)

# Operasi pengurangan
hasil_pengurangan = angka1 - angka2 - angka3
print("Hasil pengurangan:", hasil_pengurangan)

# Operasi perkalian
hasil_perkalian = angka1 * angka2 * angka3
print("Hasil perkalian:", hasil_perkalian)

# Operasi pembagian
hasil_pembagian = angka1 / angka2 / angka3
print("Hasil pembagian:", hasil_pembagian)

# Operasi pemangkatan
hasil_pemangkatan = angka1 ** angka2 ** angka3
print("Hasil pemangkatan:", hasil_pemangkatan)

print("===TUTOR YUTUB===")
a = 10
b = 3

# Operasi tambah +
hasil = a + b
print(a, '+', b, '=',hasil)

# Operasi kurang -
hasil = a - b
print(a, '-', b, '=',hasil)

# Operasi kali *
hasil = a * b
print(a, '*', b, '=',hasil)

# Operasi bagi /
hasil = a / b
print(a, '/', b, '=',hasil)

# Operasi pangkat **
hasil = a** b
print(a, '**', b, '=',hasil)

# Operasi modulus %
hasil = a % b
print(a, '%', b, '=',hasil)

# Operasi floor division //
hasil = a // b
print(a, '//', b, '=',hasil)

# prioritas operasi
'''
    1. ()
    2. exponen **
    3. perkalian dan teman-teman * / ** % //
    4. pertambahan dan pengurangan + -
'''

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, '=', hasil )

hasil = x + y * z
print(x,'+',y,'*',z, '=', hasil)
# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z
print('(', x,'+',y,') *',z, '=', hasil)