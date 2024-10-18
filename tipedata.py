# a = 10, a adalah variabel dengan nilai 10

# tipe data : Angka satuan yang gak ada koma nya (integer)
data_integer = 1
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

datainteger = 2
print("data : ", datainteger, ", bertipe : ", type(datainteger))

# tipe data : Angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

datafloat = 2.5
print("data : ", datafloat, ", bertipe : ", type(datafloat))

# tipe data : Kumpulan karakter (string)
data_string = "princess ochie 02"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

datastring = "princess ochie"
print("data : ", datastring, ", bertipe : ", type(datastring))

# tipe data : biner atau ture/false (boolean)
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

databool = False
print("data : ", databool, ", bertipe : ", type(databool))

## tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

datacomplex = complex(2,9)
print("data : ", datacomplex, ", bertipe : ", type(datacomplex))

# tipe data dari bahasa C

from ctypes import c_double, c_char

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))
